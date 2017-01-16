### Pyblish Mindbender

[![Build Status](https://travis-ci.org/pyblish/pyblish-mindbender.svg?branch=master)](https://travis-ci.org/pyblish/pyblish-mindbender) [![Coverage Status](https://coveralls.io/repos/github/pyblish/pyblish-mindbender/badge.svg?branch=master)](https://coveralls.io/github/pyblish/pyblish-mindbender?branch=master) [![PyPI version](https://badge.fury.io/py/pyblish-mindbender.svg)](https://pypi.python.org/pypi/pyblish-mindbender)

A basic asset creation pipeline - batteries included.

- [Website](http://pyblish.com/pyblish-mindbender)
- [Forums](http://forums.pyblish.com)

[![temp](https://cloud.githubusercontent.com/assets/2152766/18875905/93263c42-84bf-11e6-8c3f-7e4045d9cd9e.png)](http://pyblish.com/pyblish-mindbender)

**Install**

```bash
$ pip install pyblish-mindbender
```

Each studio must then define a few executables with their own local paths, that are later mapped into the pipeline automatically.

**mb.bat**

Main executable.

This is what artists launch at the start of any task and is from where applications are started, such as Maya and Nuke.

| Environment Variable     | Description
|:-------------------------|:----------------
| PYBLISH_MINDBENDER       | Absolute path to pyblish-mindbender
| PYBLISH_BASE			   | Absolute path to pyblish-base
| PYBLISH_MAYA             | Absolute path to pyblish-maya
| PYBLISH_NUKE             | Absolute path to pyblish-nuke
| PYBLISH_QML              | Absolute path to pyblish-qml
| PYBLISH_LITE 			   | Absolute path to pyblish-lite

**Example**

```bash
@echo off

set _GIT=M:\f03_assets\include\pyblish\git
set _MB=%_GIT%\pyblish-mindbender\bin\_mb.bat

:: Establish requirements
set PYBLISH_BASE=%_GIT%\pyblish-base
set PYBLISH_MAYA=%_GIT%\pyblish-maya
set PYBLISH_NUKE=%_GIT%\pyblish-nuke
set PYBLISH_QML=%_GIT%\pyblish-qml
set PYBLISH_LITE=%_GIT%\pyblish-lite
set PYBLISH_MINDBENDER=%_GIT%\pyblish-mindbender

:: MB Tools
set MAYA_PLUG_IN_PATH=M:\f03_assets\include\maya\scripts\Plugins;%MAYA_PLUG_IN_PATH%
set PYTHONPATH=M:\f03_assets\include\maya\scripts;%PYTHONPATH%

:: Install Nuke-specific Pyblish environment
set NUKE_PATH=M:\f03_assets\include\pyblish\etc\nuke;%NUKE_PATH%

call %_MB% M:\f01_projects %*
```

<br>

**asset.bat**

```bash
@echo off
call _mkproject %~dp0 %~n0 %1
```

<br>

### Usage

```python
>>> from pyblish_mindbender import api, maya
>>> api.install(maya)
```

- [Read more](http://pyblish.com/pyblish-mindbender)

### Testing

```bash
cd pyblish-mindbender
docker build -t pyblish/mindbender -f Dockerfile-maya2016 .

# Run nosetests (Linux/OSX)
docker run --rm -v $(pwd):/repo pyblish/mindbender
```

### Code convention

Below are some of the standard practices applied to this repositories.

- **PEP8**
 	- All code is written in PEP8. It is recommended you use a linter as you work, flake8 and pylinter are both good options.
- **Napoleon docstrings**
	- Any docstrings are made in Google Napoleon format. See [Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for details.
- **Semantic Versioning**
	- This project follows [semantic versioning](http://semver.org).
- **Underscore means private**
	- Anything prefixed with an underscore means that it is internal to wherever it is used. For example, a variable name is only ever used in the parent function or class. A module is not for use by the end-user. In contrast, anything without an underscore is public, but not necessarily part of the API. Members of the API resides in `api.py`.
