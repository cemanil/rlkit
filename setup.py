from distutils.core import setup
from setuptools import find_packages

setup(
    name='rlkit',
    version='0.1.2',
    packages=find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
)