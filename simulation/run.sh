#!/usr/bin/env bash

cp parameters.json library/parameters.json
cd library

py -u -m main

rm -r __pycache__
