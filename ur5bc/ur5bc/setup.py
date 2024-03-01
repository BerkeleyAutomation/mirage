import os
import sys

from setuptools import find_packages, setup

root_dir = os.path.dirname(os.path.realpath(__file__))

setup(name='ur5bc',
      version='0.1.0',
      description='UR5 BC', 
      package_dir = {'': '.'},
      packages=find_packages(),
     )
