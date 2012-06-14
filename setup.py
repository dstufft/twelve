#!/usr/bin/env python
from setuptools import setup
from setuptools.command.test import test as TestCommand

import twelve
import twelve.adapters
import twelve.services


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest

        pytest.main(self.test_args)

setup(
    name="twelve",
    version=twelve.__version__,
    description="12factor inspired settings for a variety of backing services archetypes.",
    long_description="\n\n".join([open("README.rst").read(), open("CHANGELOG.rst").read()]),
    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",
    url="https://crate.io/packages/twelve/",
    packages=[
        "twelve",
    ],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    install_requires=["extensions"],
    tests_require=["pytest"],
    cmdclass={"test": PyTest},
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
