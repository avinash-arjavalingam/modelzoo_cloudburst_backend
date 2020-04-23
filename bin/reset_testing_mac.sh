#!/bin/bash

cd ~/cloudburst/cloudburst
rm -rf droplet_modelzoo
rm -f testing_example.py
cd ../bin
cd ..
cp -r bin/droplet_modelzoo cloudburst/droplet_modelzoo
cp bin/testing_example.py cloudburst
cd bin
cd ../cloudburst
python3.6 testing_example.py $1 $2