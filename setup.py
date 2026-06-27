from setuptools import setup, find_packages

setup(
    name="assertix",
    version="0.1",
    packages=find_packages(),
    py_modules=["assertix"],
    entry_points={
        "console_scripts": [
            "assertix=assertix:main",
        ],
    },
)