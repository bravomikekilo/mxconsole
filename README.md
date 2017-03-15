# MXConsole
MXConsole is a standalone TensorFlow's Tensorboard port intended for MxNet, but now is **plotform netural**. Now this project is in very early stage.

## Structure
MXConsole use extracted TensorFlow's filesystem and record_reader and record_writer code
as a python extension. Thus we don't need to build the whole TensorFlow.
meanwhile, without TensorFlow's Tensor and ops. Platform relavant summary related code is needed . 
Now we only provide api that generate summary from `numpy.ndarray`. part of these api is merged from **dmlc/tensorboard**. 

## Build tools
1. bazel
1. optional: node.js (for frontend build)

## Installation
- normal installation
  1. clone this repo `git clone https://github.com/bravomikekilo/mxconsole`
  2. `cd mxconsole/tensorflow_fs`
  3. `./configure` to configure tensorflow_fs build, choose your python binary and default libs
  and choose only the jemalloc support.
  4. `cd .. && ./dev_build.sh` 
  5. Add this repo to your `PATHONPATH`.
  6. You now can use the MXConsole like `python -m mxconsole --logdir path/of/your/logs`

- develop build(build from source) **do this only when you have changed the frontend**
  1. clone this repo `$ git clone https://github.com/bravomikekilo/mxconsole`
  2. `$ cd mxconsole/tensorflow_fs`
  3. `$ ./configure` to configure tensorflow_fs build, choose your python binary and default libs
  and choose only the jemalloc support.
  4. `$ cd .. && ./dev_build.sh` 
  5. `$ sudo python setup.py install`
  6. You now can use the MXConsole like 
    `$ python -m mxconsole --logdir path/of/your/logs`

- refresh the native library
  1. `$ ./update_native.sh`

some logs can be generated from **carpedm20/DCGAN-tensorflow**, just train that model on mnist is just fine.
You also can try the example merged from **dmlc/tensorboard**, under the demo folder.