#! /usr/bin/env python3

"""
<Program Name>
  setup.py

<Author>
  Vladimir Diaz <vladimir.v.diaz@gmail.com>

<Started>
  December 7, 2016.

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  BUILD SOURCE DISTRIBUTION

  The following shell command generates a securesystemslib source archive that
  can be distributed to other users.  The packaged source is saved to the
  'dist' folder in the current directory.

  $ python setup.py sdist


  INSTALLATION OPTIONS

  pip - installing and managing Python packages (recommended):

  # Installing from Python Package Index (https://pypi.python.org/pypi).
  $ pip install securesystemslib

  # Installing from local source archive.
  $ pip install <path to archive>

  # Or from the root directory of the unpacked archive.
  $ pip install .

  Alternate installation options:

  Navigate to the root directory of the unpacked archive and
  run one of the following shell commands:

  Install to the global site-packages directory.
  $ python setup.py install

  Install to the user site-packages directory.
  $ python setup.py install --user

  Install to a chosen directory.
  $ python setup.py install --home=<directory>


  Note: The last two installation options may require modification of
  Python's search path (i.e., 'sys.path') or updating an OS environment
  variable.  For example, installing to the user site-packages directory might
  result in the installation of scripts to '~/.local/bin'.  The user may
  then be required to update his $PATH variable:
  $ export PATH=$PATH:~/.local/bin
"""

from setuptools import setup

if __name__ == "__main__":
  setup()
