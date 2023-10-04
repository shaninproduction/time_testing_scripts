#!/bin/bash

./clean_builds.sh
./clean_preproc.sh
./build_apps.sh "500 1000 1500 2000 2500"
./update_data.sh "500 1000 1500 2000 2500" "O0 O2" 20
python3 make_preproc.py
python3 make_postproc.py