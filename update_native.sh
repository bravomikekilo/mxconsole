#! /usr/bin/env bash
# script used for update the tensorflow_fs extension
cd tensorflow_fs
./build.sh
cd ..
echo "removing old native library"
rm mxconsole/lib/native/pywrap*
rm mxconsole/lib/native/_pywrap*
echo "clean finish"
cp tensorflow_fs/bin/pywrap_tensorflow_fs.py \
   tensorflow_fs/bin/_pywrap_tensorflow_fs.so \
   mxconsole/lib/native/
echo "done"