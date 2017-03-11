#! /usr/bin/env bash
# script used for update the tensorflow_fs extension
cd tensorflow_fs
bazel build -c opt //tensorflow/python:pywrap_tensorflow_fs
cd ..
echo "removing old native library"
rm mxconsole/lib/native/pywrap*
rm mxconsole/lib/native/_pywrap*
echo "clean finish"
cp tensorflow_fs/bazel-bin/tensorflow/python/pywrap_tensorflow_fs.py \
   tensorflow_fs/bazel-bin/tensorflow/python/_pywrap_tensorflow_fs.so \
   mxconsole/lib/native/
echo "done"