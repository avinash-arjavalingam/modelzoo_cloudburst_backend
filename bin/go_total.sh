#!/bin/bash

cd ~/cloudburst/bin
bash go_clean.sh
bash go_start.sh $1 $2
bash go_run.sh
bash go_test.sh
bash go_clean.sh
