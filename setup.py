#!/usr/bin/env python3
from setuptools import setup, Extension

enhance_module = Extension("vimiv._image_enhance", sources=["c-lib/enhance.c"])

setup(ext_modules=[enhance_module])
