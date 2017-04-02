#! /usr/bin/env bash
sudo rm -r build dist MXConsole.egg-info/
sudo -H pip3 uninstall mxconsole
sudo python3 setup.py install
