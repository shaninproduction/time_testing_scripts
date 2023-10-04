#!/bin/bash

# "11000 11500 12000 16000 18000"

#default sizes
sizes="500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000 10500 11000 12500 13000 13500 14000 14500 15000 15500 16500 17000 17500 18500 19000 19500 20000"

#default opts
opts="O0 O2"

#default count
count=1000


flag=0

if [ ! -z "$1" ]; then
    sizes="$1"
    flag=1
fi

if [ ! -z "$2" ]; then
    opts="$2"
    flag=1
fi

if [ ! -z "$3" ]; then
    count="$3"
    flag=1
fi

if [[ $flag -eq 1 ]]; then
    ./build_apps.sh "$sizes" "$opts"
fi

for num in $(seq "$count"); do
    for file in ./programms/*; do    
        for opt in $opts; do
            for size in $sizes; do
                printf "$num/$count ${file:12:-2} $size \r"
                ./apps/"${file:12:-2}_${size}_${opt}.exe" >> ./data/"${file:12:-2}_${size}_${opt}.txt" 
            done
        done
    done
done
