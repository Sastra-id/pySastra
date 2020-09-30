"""Module setup."""

import runpy
from setuptools import setup, find_packages

PACKAGE_NAME = "pysastra"
version_meta = runpy.run_path("./version.py")
VERSION = version_meta["__version__"]


with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename): 
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION, 
        packages=find_packages(exclude=("tests",)),
        author="Fahmi Rasyid",
        author_email="ufarasfa@gmail.com",
        install_requires=parse_requirements("requirements.txt"),
        python_requires=">=3.6.3",  
        url="https://github.com/sastra-id/pysastra",
        license="MIT",
        description="Lightweight Natural Language Processing for Indonesian Language.",
        long_description=long_description,
        long_description_content_type="text/markdown",
    )
