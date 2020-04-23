#!/bin/bash

cd ~/cloudburst/bin/droplet-go
mv test_load.bts ../../cloudburst
cd ../../cloudburst
python3.6 load_bits.py
