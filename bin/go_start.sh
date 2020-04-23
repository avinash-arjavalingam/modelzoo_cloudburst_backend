#!/bin/bash

cd ~/cloudburst
python3.6 dump_bits.py $2
cd bin
bash reset_testing_mac.sh $1 $2
mv ../test_dump.bts droplet-go
