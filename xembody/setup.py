import os
import sys

from setuptools import find_packages, setup

root_dir = os.path.dirname(os.path.realpath(__file__))

setup(
    name='xembody',
    version='0.1',
    description='Repo for Mirage',
    author='Lawrence Chen, Karthik Dharmarajan, Kush Hari',
    package_dir = {'': '.'},
    packages=find_packages(include=['xembody', 'xembody.*', 'xembody_robosuite', 'xembody_robosuite.*']),
    install_requires=[
        "numpy",
        "pyyaml",
    ],
    extras_require={
        "docs": [
            "sphinx",
            "pydata-sphinx-theme"
        ]
    }
)