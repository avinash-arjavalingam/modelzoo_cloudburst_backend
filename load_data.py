#!/usr/bin/python3.6

import os
import sys
import pickle
import cloudpickle as cp
import codecs
from PIL import Image 

inp = Image.open("/hydro_test/test_image.jpg")
with open("test_dump.bts", 'wb') as file:
	cp.dump(inp, file)