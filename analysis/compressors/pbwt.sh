#!/bin/bash

set -e

input_file=$1
output_file=$2

SECONDS=0
/usr/bin/pbwt zip --delete-output "$input_file" "$output_file"
exec_time="$SECONDS"

input_size=$(stat -c%s "$input_file")
output_size=$(stat -c%s "$output_file")

echo "RESULTS: input_size=$input_size,output_size=$output_size,exec_time=$exec_time"