#!/usr/bin/python3.6

import sys
import time
import json
import numpy as np
import torch
import pandas as pd
from PIL import Image
import torchvision
import pickle
from torch.nn import Parameter
import codecs
import anna
from anna.client import AnnaTcpClient
from anna.lattices import LWWPairLattice
# import droplet
# from anna.shared.serializer import Serializer

client = AnnaTcpClient('127.0.0.1', '127.0.0.1', local=True, offset=2)
model_options = ['ResNet50', 'ResNet18', 'ResNet152']

# value_string = "World"
# value = LWWPairLattice(1, value_string.encode())
# client.put("Hello", value)
# ret = (((client.get("Hello"))["Hello"]).reveal()).decode()
# print(ret)

model_str = str(sys.argv[1])
load_str = ''
if(model_str == model_options[0]):
	load_str = '/hydro_test/model_weights/resnet50-19c8e357.pth'
elif(model_str == model_options[1]):
	load_str = '/hydro_test/model_weights/resnet18-5c106cde.pth'
elif(model_str == model_options[2]):
	load_str = '/hydro_test/model_weights/resnet152-b121ed2d.pth'

temp = torch.load(load_str)
with open("torch_file.txt", "w") as file:
    file.write(str(temp))
temp_param = temp
# temp_param = list(temp.items())[0]
# 0:266
temp_super = temp_param
temp_pickle_string = ''.join((codecs.encode(pickle.dumps(temp_super), "base64").decode()).split())
# temp_pickle_string = (codecs.encode(pickle.dumps(temp_super), "base64").decode())
# temp_string = np.array2string(temp_super.data[0].numpy(), separator=',')
# print(type(list(temp.items())[0][1]))
# print(super(Parameter, temp_param).__repr__())
pickle_arr = []
pickle_len = len(temp_pickle_string)
# running_end = (running_beg + 4000) if (pickle_len > (running_beg + 4000)) else pickle_len
for i in range(0, pickle_len, 4000):
	j = (i + 4000) if ((i + 4000) < pickle_len) else pickle_len
	pickle_arr.append(temp_pickle_string[i:j])
print(temp_super)
# print(len(list(temp_super.data)))
# print(repr(temp_string))
# with open("temp_string_holder.txt", "w") as file:
#     file.write(temp_string)

# print(temp_pickle_string)
base_string = model_str
bash_bytes_string = model_str + "#Index"
i = 0
"""
for temp_string_iter in pickle_arr:
	key_string = base_string + "#" + str(i)
	value_bytes = LWWPairLattice(int(time.time()), temp_string_iter.encode())
	client.put(key_string, value_bytes)
	print(key_string)
	# print(temp_string_iter)
	# print("")
	i += 1
i_string = str(i)
i_bytes = LWWPairLattice(int(time.time()), i_string.encode())
client.put(bash_bytes_string, i_bytes)
"""

i_two = int((((client.get(bash_bytes_string))[bash_bytes_string]).reveal()).decode())
temp_pickle_ret = ""
for index in range(i_two):
	temp_string_iter_two = pickle_arr[index]
	key_string_two = base_string + "#" + str(index)
	ret = (((client.get(key_string_two))[key_string_two]).reveal()).decode()
	temp_pickle_ret = temp_pickle_ret + ret
	print(temp_string_iter_two == ret)

# print(bin(temp_pickle_string))
print(type(temp_pickle_string))
# print(len(list(str.split(temp_pickle_string))))
# print(list(temp.items())[0][1])
# print(list(temp.items())[0])
# print(list(temp.items()))
# print(type(temp))
# print(temp_pickle_string)
temp_recon = pickle.loads(codecs.decode(temp_pickle_ret.encode(), "base64"))
print(temp_recon)
print(type(temp_recon))
