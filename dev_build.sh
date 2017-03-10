cd tensorflow_fs
bazel build -c opt //tensorflow/python:pywrap_tensorflow_fs
cd ..
rm lib/native/pywrap*
rm lib/native/_pywrap*
cp tensorflow_fs/bazel-bin/tensorflow/python/pywrap_tensorflow_fs.py \
   tensorflow_fs/bazel-bin/tensorflow/python/_pywrap_tensorflow_fs.so \
   lib/native/
sudo npm install
typings install
gulp compile
bower install
