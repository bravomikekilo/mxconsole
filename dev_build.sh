#! /usr/bin/env bash
cd tensorflow_fs
bazel build -c opt //tensorflow/python:pywrap_tensorflow_fs
cd ..
echo "update the native library"
./update_native.sh
echo "finish update the native library"
echo "update frontend components"
sudo npm install
typings install
gulp compile
bower install
echo "finish"
cd ..
sudo python setup.py install