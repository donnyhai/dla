#!/usr/bin/env bash

cp parameters.txt library/parameters.txt
cd library

py -u -m main

rm parameters.txt
rm -r __pycache__

cd ..
cp library/*.png images
rm -r library/*.png

cp library/*.txt images
rm -r library/*.txt