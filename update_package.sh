sudo -H pip3 uninstall mxconsole
python3 setup.py bdist_wheel
sudo -H pip3 install dist/MXConsole-0.0.1a1-py2.py3-none-any.whl
