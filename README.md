# MXConsole
MXConsole is a standalone TensorFlow's Tensorboard port intended for MxNet, but now is **plotform netural**. Now this project is in very early stage.

## Structure
MXConsole use extracted TensorFlow's filesystem and record_reader and record_writer code
 as a python extension. Thus we don't need to build the whole TensorFlow.
 meanwhile, without TensorFlow's Tensor and ops. Platform relavant summary related code is needed . 
 Such as **dmlc/tensorboard**. MXConsole now can only present logs by now.

## Installation
1. clone this repo `git clone https://github.com/bravomikekilo/mxconsole`
2. cd mxconsole/tensorflow_fs
3. `./configure` to configure tensorflow_fs build, choose your python binary and default libs
  and choose only the jemalloc support.
4. `cd .. && ./build.sh` 
2. Add this repo to your `PATHONPATH`.
3. You now can use the MXConsole like `python -m mxconsole --logdir path/of/your/logs`

some logs can be generated from **carpedm20/DCGAN-tensorflow**, just train that model on mnist is just fine.
