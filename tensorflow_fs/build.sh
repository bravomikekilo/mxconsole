bazel build -c opt //tensorflow/python:pywrap_tensorflow_fs
cd ..
rm mxconsole/lib/native/pywrap*
rm mxconsole/lib/native/_pywrap*
cp  tensorflow_fs/bazel-bin/tensorflow/python/pywrap_tensorflow_fs.py \
    tensorflow_fs/bazel-bin/tensorflow/python/_pywrap_tensorflow_fs.so \
    mxconsole/lib/native/
