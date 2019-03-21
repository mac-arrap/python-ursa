# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="ursa",
    version="0.1.0",
    description="python wrapper for ursa universal crypto library",
    license="apache2",
    author="Cam Parra",
    packages=find_packages(),
    install_requires=["pytest"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ]
)
