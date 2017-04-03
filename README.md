# MXConsole
MXConsole is a standalone TensorFlow's Tensorboard port intended for MxNet, but now is **plotform netural**. Now this project is in very early stage.

## Structure
MXConsole use extracted TensorFlow's filesystem and record_reader and record_writer code
as a python extension. Thus we don't need to build the whole TensorFlow.
meanwhile, without TensorFlow's Tensor and ops. Platform relavant summary related code is needed . 
Now we only provide api that generate summary from `numpy.ndarray`. part of these api is merged from **dmlc/tensorboard**. 

## Build tools
1. bazel
2. node.js and bower(actually we only need bower to do bower install, so just `npm install -g bower` should be fine`)
3. optional: gulp and other node.js module(for frontend build only)

## Installation
- normal installation
  1. clone this repo `git clone https://github.com/bravomikekilo/mxconsole --recursive`
  2. `cd mxconsole/tensorflow_fs`
  3. `./configure` to configure tensorflow_fs build, choose your python binary and default libs
  and choose only the jemalloc support.
  4. `cd .. && ./update_native.sh` to build and update tensorflow_fs
  4. `python setup.py setup.py bdist_wheel` to build python wheel
  5. `pip install dist/MXConsole-0.0.1a1-py2.py3-none-any.whl`  install the python wheel
  6. You now can use the MXConsole like `python -m mxconsole --logdir path/of/your/logs`

- refresh the native library
  1. `$ ./update_native.sh`

some logs can be generated from **carpedm20/DCGAN-tensorflow**, just train that model on mnist is just fine.
You also can try the example merged from **dmlc/tensorboard**, under the demo folder.
