#!/bin/bash

./clean_builds.sh
./clean_preproc.sh
./build_apps.sh "50 100 150 200 250"
./update_data.sh "50 100 150 200 250" "O0" 20
python3 make_preproc.py
python3 make_postproc.py