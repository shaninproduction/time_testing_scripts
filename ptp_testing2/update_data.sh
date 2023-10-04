#!/bin/bash


#default sizes
sizes="50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800"

#default opts
opts="O0"

#default count
count=5000


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
