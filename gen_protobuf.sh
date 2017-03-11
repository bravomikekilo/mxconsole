#! /usr/bin/env bash
# a develop tool to generate protobuf python lib for mxconsole 
filenames=(`ls mxconsole/protobuf | grep ".*\.proto"`)

for file in ${filenames[@]}; do
    echo $file
    protoc mxconsole/protobuf/$file --python_out=.
done
