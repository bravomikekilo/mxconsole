# MXConsole
MXConsole is a standalone TensorFlow's Tensorboard port intended for MxNet, but now is **plotform netural**. Now this project is under very early stage.

## Structure
MXConsole use extracted TensorFlow's filesystem and record_reader and record_writer code
 as a python extension. Thus we don't need to build the whole TensorFlow.
 meanwhile, without TensorFlow's Tensor and ops. We need to make our own summary related code. 
 Such as **dmlc/tensorboard**. MXconsole now can only present logs by now.

## Installation
1. Run `./build.sh` 
2. Add cloned repo to your `PATHONPATH`.
3. You now can use the mxconsole like `python3 -m mxconsole --logdir path/of/your/logs`

some logs can be generated from **carpedm20/DCGAN-tensorflow**, just train that model on mnist is just fine.
