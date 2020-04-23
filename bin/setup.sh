#!/bin/bash

mkdir /Users/Avi/cloudburst/anna
git clone --recurse-submodules https://github.com/hydro-project/anna.git /Users/Avi/cloudburst/anna
mkdir /Users/Avi/cloudburst/cloudburst
git clone --recurse-submodules https://github.com/hydro-project/cloudburst.git /Users/Avi/cloudburst/cloudburst
# docker run -v ~/cloudburst:/hydro_test -it vsreekanti/anna bash