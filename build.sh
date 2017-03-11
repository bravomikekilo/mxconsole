#! /usr/bin/env bash
echo "update the native library"
./update_native.sh
echo "finish update the native library"
echo "update the frontend components"
cd mxconsole
bower install
echo "finished"