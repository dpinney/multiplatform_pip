from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os

def system_install():
	os.system('touch blahblahblah.txt')

class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        system_install()

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        system_install()

setup(
    name='mpp',
    version='1.0.0',
    url='https://github.com/dpinney/multiplatform_pip',
    author='David Pinney',
    author_email='none@none.com',
    description='Example of a python package with multiplatform statically linked libraries.',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True)
