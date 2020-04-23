#!/usr/bin/python3.6

import os
import sys
import pickle
import cloudpickle as cp
import codecs
from PIL import Image 

# from cloudburst.shared.serializer import Serializer
# ser = Serializer()

inp = Image.open(str(sys.argv[1]))

with open("test_dump.bts", 'wb') as file:
        cp.dump(inp, file)
        # file.write(file_bytes)

