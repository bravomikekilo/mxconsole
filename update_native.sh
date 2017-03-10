cd tensorflow_fs
bazel build -c opt //tensorflow/python:pywrap_tensorflow_fs
cd ..
echo "removing old native library"
rm lib/native/pywrap*
rm lib/native/_pywrap*
echo "clean finish"
cp tensorflow_fs/bazel-bin/tensorflow/python/pywrap_tensorflow_fs.py \
   tensorflow_fs/bazel-bin/tensorflow/python/_pywrap_tensorflow_fs.so \
   lib/native/
echo "done"