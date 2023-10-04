#!/bin/bash

#default sizes
sizes="500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000"

#default opts
opts="O0 O2"

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
