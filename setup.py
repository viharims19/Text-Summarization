from setuptools import find_packages, setup

setup(
    name = 'TxtSmrzr',
    version= '0.0.0',
    author= 'vihari',
    author_email= 'sai.vihari95@gmail.com',

    package_dir={"": "src"},
    packages= find_packages(where="src")

)