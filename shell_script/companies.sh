#!/bin/bash

URL="https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"

curl -s "$URL" | awk -F',' '
BEGIN {
    OFS=","
}

NR==1{
    for(i=1;i<=NF;i++){
        if($i=="Security") company=i
        if($i=="Headquarters Location") location=i
        if($i=="Founded") founded=i
    }
    next
}

{
    print $company,$location,$founded
}
' | sort -t',' -k3,3n