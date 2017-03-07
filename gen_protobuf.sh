#! /usr/bin/env bash
cd ..
filenames=(`ls mxconsole/protobuf | grep ".*\.proto"`)

for file in ${filenames[@]}; do
    echo $file
    protoc mxconsole/protobuf/$file --python_out=.
done
