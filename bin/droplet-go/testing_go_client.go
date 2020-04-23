package main

import (
	"fmt"
	"os"
	client "github.com/cloudburstclient"
	. "github.com/proto/common"
)

func main() {
    file, _ := os.Open("test_dump.bts")
    stat, _ := file.Stat()
    size := stat.Size()
    inpData := make([]byte, size)
    fmt.Println(size)
    file.Read(inpData)
    // fmt.Println(inpData)
    file.Close()
    // fmt.Println(inpData)

    testing_client := client.NewCloudburstClient("127.0.0.1", "127.0.0.1", true)

    argsMap := map[string]*Arguments{}
    args := &Arguments{}
    args.Values = append(args.Values, &Value{Body: inpData, Type: SerializerType_DEFAULT})
    argsMap["torch_class"] = args

    output := (testing_client.CallDag("torch_dag", argsMap, true)).Get()
    file_two, _ := os.Create("test_load.bts")
    fmt.Println(len(*output))
    // out_len = len(*output)

    // stat_two, _ := file_two.Stat()
    // _ := stat_two.Size()
    file_two.Write(*output)
    file_two.Close()
    fmt.Println(*output)

	/*
    testing_client := NewCloudburstClient("127.0.0.1", "127.0.0.1", true)
    args := make(map[string]*Arguments)
    var single_st SerializerType = 0
    single_bytes := []byte{1}
    single_value := Value{Body: single_bytes, Type: single_st}
    single_arg := Arguments{Values: []*Value{&single_value}}
    args["incr"] = &single_arg
    output := testing_client.CallDag("test_dag", args, true)
    fmt.Println(output)
    // fmt.Println("Hello World")
    */
}
