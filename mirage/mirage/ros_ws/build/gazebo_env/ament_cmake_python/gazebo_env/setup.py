from setuptools import find_packages
from setuptools import setup

setup(
    name='gazebo_env',
    version='0.0.0',
    packages=find_packages(
        include=('gazebo_env', 'gazebo_env.*')),
)
