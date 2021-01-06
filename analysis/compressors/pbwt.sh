#!/bin/bash

input_file=$1
output_file=$2

SECONDS=0
pbwt zip "$input_file" "$output_file"
exec_time="$SECONDS"

input_size=$(stat -c%s "$input_file")
output_size=$(stat -c%s "$output_file")

echo "input_size=$input_size,output_size=$output_size,exec_time=$exec_time"