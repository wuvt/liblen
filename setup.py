from setuptools import setup

setup(
    name="liblen",
    version="1.0",
    py_modules=["liblen"],
    description="Tools for working with Len's spreadsheets",
    license="GPLv3",
    url="https://github.com/wuvt/liblen",
    install_requires=["xlrd"]
)
