from setuptools import setup, find_packages

setup(
    name='mpp',
    version='1.0.0',
    url='https://github.com/dpinney/multiplatform_pip',
    author='David Pinney',
    author_email='none@none.com',
    description='Example of a python package with multiplatform statically linked libraries.',
    packages=find_packages(),    
    install_requires=[],
)