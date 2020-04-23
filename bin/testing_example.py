#!/usr/bin/python3.6

import sys
import torch
from PIL import Image
from cloudburst.client.client import CloudburstConnection
from droplet_modelzoo import Torch_Class

local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', tid=20, local=True)
torch_init_arg = [str(sys.argv[1])]
torch_init_arg_two = (torch_init_arg,)
torch_class = local_cloud.register((Torch_Class, torch_init_arg_two), 'torch_class')
local_cloud.register_dag('torch_dag', ['torch_class'], [])
# inp = Image.open("/Users/Avi/cloudburst/" + str(sys.argv[2]))
# print("Torch class incr get: " + str(torch_class(inp).get()))
# print("Torch dag incr get" + str(local_cloud.call_dag('torch_dag', {'torch_class': inp}).get()))
print(str(sys.argv[2]))


# cloudburst = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
# incr = lambda _, a: a + 1
# cloud_incr = cloudburst.register(incr, 'incr')
# print(cloud_incr(1).get())
# square = lambda _, a: a * a
# cloud_square = cloudburst.register(square, 'square')
# print(cloud_square(2).get())
