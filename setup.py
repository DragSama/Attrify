import re
from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("superdict/__init__.py") as file:
    version = re.search("__version__ = (\S+)", file.read()).group(1)

setup(
    name="superdict",
    description="Convert dict to access dict keys as attributes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DragSama/SuperDict",
    author="DragSama",
    version=version,
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    keywords="dict python3 superdict attributes ",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
