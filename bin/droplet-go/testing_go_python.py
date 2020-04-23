#!/usr/bin/python3.6

import codecs
import cloudpickle as cp
from cloudburst.client.client import CloudburstConnection

local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
incr = lambda _, a: a + 1
cloud_incr = local_cloud.register(incr, 'incr')
square = lambda _, a: a * a
cloud_square = local_cloud.register(square, 'square')
local_cloud.register_dag('test_dag', ['incr', 'square'], [('incr', 'square')])
val = local_cloud.call_dag('test_dag', { 'incr': 1 }).get()
print(val)
