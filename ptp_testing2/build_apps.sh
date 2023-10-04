#!/bin/bash

#default sizes
sizes="50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800"

#default opts
opts="O0"

if [ ! -z "$1" ]; then
    sizes=$1
fi

if [ ! -z "$2" ]; then
    opts=$2
fi


for file in ./programms/*; do
    for opt in $opts; do
        for size in $sizes; do
            gcc -std=c99 -DNMAX="${size}" -"${opt}" \
                "${file}" -o ./apps/"${file:12:-2}"_"${size}"_"${opt}".exe 
        done
    done
done
