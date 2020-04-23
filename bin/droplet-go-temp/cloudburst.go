package main

import (
	"fmt"

	"github.com/golang/protobuf/proto"
	zmq "github.com/pebbe/zmq4"
	. "github.com/proto/common"
)

const (
	connectPort    = 5000
	funcCreatePort = 5001
	funcCallPort   = 5002
	listPort       = 5003
	dagCreatePort  = 5004
	dagCallPort    = 5005
	dagDeletePort  = 5006
)

type CloudburstClient struct {
	schedulerAddress string
	ipAddress        string
	responseAddress  string
	localMode        bool

	kvsClient      *AnnaClient
	dagCallSocket  *zmq.Socket
	responseSocket *zmq.Socket
}

func NewCloudburstClient(schedulerAddress string, ipAddress string, localMode bool) *CloudburstClient {
	context, _ := zmq.NewContext()
	kvsAddress := connect(schedulerAddress, context)
	kvsClient := NewAnnaClient(kvsAddress, ipAddress, localMode)

	dagCallSocket, _ := context.NewSocket(zmq.REQ)
	dagCallSocket.Connect(fmt.Sprintf(pushTemplate, schedulerAddress, dagCallPort))

	responseSocket, _ := context.NewSocket(zmq.PULL)
	responseSocket.Bind(fmt.Sprintf(pullTemplate, 9000))

	responseAddress := fmt.Sprintf(pushTemplate, ipAddress, 9000)

	return &CloudburstClient{
		schedulerAddress: schedulerAddress,
		ipAddress:        ipAddress,
		responseAddress:  responseAddress,
		localMode:        localMode,
		dagCallSocket:    dagCallSocket,
		responseSocket:   responseSocket,
		kvsClient:        kvsClient,
	}
}

func connect(schedulerAddress string, context *zmq.Context) string {
	connectSocket, _ := context.NewSocket(zmq.REQ)
	connectSocket.Connect(fmt.Sprintf(pushTemplate, schedulerAddress, connectPort))
	connectSocket.Send("", zmq.DONTWAIT)
	kvsAddress, _ := connectSocket.Recv(zmq.DONTWAIT)

	return kvsAddress
}

func (cloudburst *CloudburstClient) CallDag(name string, arguments map[string]*Arguments, directResponse bool) *CloudburstFuture {
	call := &DagCall{
		Name:         name,
		FunctionArgs: arguments,
	}

	if directResponse {
		call.ResponseAddress = cloudburst.responseAddress
	}

	serialized, _ := proto.Marshal(call)
	cloudburst.dagCallSocket.SendBytes(serialized, 0)

	bts, _ := cloudburst.dagCallSocket.RecvBytes(0)
	response := &GenericResponse{}
	proto.Unmarshal(bts, response)

	future := &CloudburstFuture{
		kvsClient: cloudburst.kvsClient,
		objectId:  response.ResponseId,
	}

	if directResponse {
		bts, _ := cloudburst.responseSocket.RecvBytes(0)
		future.data = &bts
	}

	return future
}

type CloudburstFuture struct {
	kvsClient *AnnaClient
	objectId  string
	data      *[]byte
}

func (future *CloudburstFuture) Get() *[]byte {
	for len(*future.data) == 0 {
		lattice := future.kvsClient.Get(future.objectId)
		if lattice != nil {
			lww := lattice.(*LWWLattice)
			future.data = &lww.Value
		}
	}

	return future.data
}
