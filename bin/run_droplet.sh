#!/bin/bash

cd /hydro_test/cloudburst
bash common/scripts/install-dependencies.sh
pip install -r requirements.txt
cd ..
echo y | sudo apt-get install python-setuptools
echo y | sudo apt-get install libzmq3-dev
pip3 install numpy
pip3 install pandas
pip3 install flask
pip3 install flask_cors
pip3 install Pillow==6.1
pip3 install transformers
pip3 install torchvision
pip3 install w3lib
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION='python'
cd anna
bash scripts/build.sh
bash scripts/start-anna-local.sh no no
cd ../cloudburst
bash scripts/clean.sh
bash scripts/build.sh
bash scripts/install-anna.sh
bash scripts/start-cloudburst-local.sh no
