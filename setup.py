from setuptools import setup, find_packages

description = ('A Python implementation of the QFT for QISKIT.')

setup(
  name='qiskit-qft',
  version='0.1.0',
  author='HTGAzureX1212',
  description=description,
  packages=find_packages(),
  install_requires=[
    'qiskit'
  ]
)
