#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension, os


def install():
    return os.system("./scripts/download.sh")

if not os.path.exists("./RNNLM_pyWrap"):
    install()

try:
    with open("README.rst") as f:
        long_description = f.read()
except IOError:
    long_description = ""


setup(
    name="RNNLM_pyWrap",
    version="0.2.3",
    author="Mohamed Zahran",
    author_email="moh.a.zahran@gmail.com",
    description="python wrapper for RNNLM Toolkit (http://rnnlm.org/)",
    long_description=long_description,
    url="https://github.com/mohazahran/RNNLM_pyWrap",
    license="MIT",
    py_modules=["RNNLM_pyWrap"],
    ext_modules=[
        Extension(
            "_RNNLM_pyWrap",
            sources=["./pythonWrap/rnnlm_wrap.cxx", "./pythonWrap/rnnlmlib.cpp"]
        )
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing :: Linguistic",
    ],
)
