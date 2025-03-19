from setuptools import setup, find_packages

setup(
    name="calculator-package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Aditya Pandey",
    author_email="adityaadityapandey2002@gmail.com",
    description="A simple calculator package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/calculator-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
