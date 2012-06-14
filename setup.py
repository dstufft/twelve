#!/usr/bin/env python
import twelve
import twelve.adapters
import twelve.services

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="twelve",
    version=twelve.__version__,
    description="12factor inspired settings for a variety of backing services archetypes.",
    long_description=open("README.rst").read() + '\n\n' +
                     open("CHANGELOG.rst").read(),
    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",
    url="https://crate.io/packages/twelve/",
    packages=[
        "twelve",
    ],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    install_requires=[
        "extensions"
    ],
    license=open("LICENSE").read(),
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
    ),
)
