#!/usr/bin/env python
# coding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=csr_gen,
    version=0.1,
    packages=["csrgen"],
    url="https://github.com/cristianowa/csr_generator",
    #license=LICENSE,
    author="Cristiano Werner Araújo",
    author_email="cristianowerneraraujo@gmail.com",
    description="Command line tool to generate CSR(certificate signing request) with less pain",
    long_description=open('README.md').read(),
)
