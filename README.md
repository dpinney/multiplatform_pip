# multiplatform_pip

Simple test for isolated multi-platform pip installs. The package has no requirements as pip sees them, but on first run it will install a difficult platform dependency in its own /lib folder.

## How to Install and Test

```python3 -m pip install "https://github.com/dpinney/multiplatform_pip/archive/main.zip"```

Or pretty sure git-mode will work in case you want to edit:

```python3 -m pip install git+https://github.com/dpinney/multiplatform_pip.git```

And then to test, i.e. run some simple numpy calculations:

```python3 -c "import mpp"```
