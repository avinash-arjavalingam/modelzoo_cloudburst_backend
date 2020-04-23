#!/bin/bash

cd ~/cloudburst/cloudburst
bash common/scripts/install-dependencies-osx.sh
pip install -r requirements.txt
pip3.6 install -r requirements.txt
cd ..
brew install zmq
pip3.6 install numpy
pip3.6 install pandas
pip3.6 install flask
pip3.6 install flask_cors
pip3.6 install Pillow==6.1
pip3.6 install transformers
pip3.6 install torchvision
pip3.6 install w3lib
pip3.6 install ipython pyzmq tornado
echo y | pip3.6 uninstall protobuf
echo y | pip3.6 uninstall google
pip3.6 install google
pip3.6 install protobuf
pip3.6 install pyyaml
pip3.6 install cloudpickle
cd anna
bash scripts/build.sh
bash scripts/start-anna-local.sh no no
cd ../cloudburst
bash scripts/clean.sh
bash scripts/build.sh
bash scripts/install-anna.sh
bash scripts/start-cloudburst-local.sh no
