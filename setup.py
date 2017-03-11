import os
from setuptools import setup, find_packages
LONG_DESCRIPTION = """
"""
setup(
    name="MXConsole",
    version="0.0.1a1",
    description="A standalone tensorboard port for mxnet and other framework",
    long_description=LONG_DESCRIPTION,
    author="google bravomikekilo",
    author_email='bravomikekilo@buaa.edu.cn',
    license='Apache-2.0',
    url='https://github.com/bravomikekilo/mxconsole',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='mxnet visualzation tensorboard standalone',
    packages=find_packages(exclude=['mxconsole.scripts']),
    install_requires=['pillow', 'numpy'],
    package_data={
    	'lib.native': ['_pywrap_tensorflow_fs.so'],
    	'mxconsole': ['bower_components/*'],
    	'mxconsole': ['dist/*'],
    }
)
