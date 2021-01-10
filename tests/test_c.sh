#!/bin/bash

ROOT_DIR=$(pwd)
cd "$ROOT_DIR" || exit 1

test_file="$ROOT_DIR"/tests/examples/world192.txt
out_file=${test_file%.*}.pbwt
tmp_file=${test_file%.*}.unpbwt

./cpbwt zip "$test_file" "$out_file" 1 p
./cpbwt unzip "$out_file" "$tmp_file"
./cpbwt compare "$test_file" "$tmp_file"
result=$?

rm -f "$out_file"
rm -f "$tmp_file"

if [[ "$result" -eq 0 ]]; then
  echo "PBWT - TEST SUCCESS"
  exit 0
else
  echo "PBWT - TEST FAILED"
  exit 1
fi
