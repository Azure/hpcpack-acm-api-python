# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "hpc-acm"
VERSION = "1.3.1"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author="Microsoft HPC Pack",
    author_email="hpccoree@microsoft.com",
    url="https://github.com/Azure/hpcpack-acm-api-python",
    description="HPC Web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    package_data={
        'hpc_acm': ['3rdpartylicenses.txt']
    },
)
