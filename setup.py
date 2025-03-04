#!/usr/bin/env python3
"""
A static website generator for people who enjoy the simpler things in life.

* `Github <https://github.com/dmulholl/ark>`_
* `Documentation <http://www.dmulholl.com/docs/ark/master/>`_
* `Demo <http://www.dmulholl.com/demos/ark/>`_

"""

import os
import re
import io
import setuptools


# MANIFEST.in file content.
manifest = """\
include license.txt readme.md
recursive-include ark/extensions *
recursive-include ark/bundle *
"""


# Write a temporary MANIFEST.in file alongside the setup.py file.
manpath = os.path.join(os.path.dirname(__file__), 'MANIFEST.in')
with io.open(manpath, 'w', encoding='utf-8') as manfile:
    manfile.write(manifest)


# Load the package's metadata into the meta dict.
metapath = os.path.join(os.path.dirname(__file__), 'ark', '__init__.py')
with io.open(metapath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))


# Standard setup routine.
setuptools.setup(
    name = 'ark',
    version = meta['version'],
    packages = setuptools.find_packages(),
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'ark = ark:main',
        ],
    },
    install_requires = [
        'markdown ~= 3.0',
        'pygments ~= 2.0',
        'pyyaml ~= 6.0',
        'jinja2 ~= 3.0',
        'syntext ~= 3.0',
        'ibis ~= 3.0',
        'shortcodes ~= 5.1',
        'argslib ~= 2.0',
        'colorama ~= 0.4',
    ],
    python_requires = ">=3.10",
    author = 'Darren Mulholland',
    url='https://github.com/dmulholl/ark',
    license = 'Public Domain',
    description = 'A static website generator for people who enjoy the simpler things in life.',
    long_description = __doc__,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)


# Delete the temporary MANIFEST.in file.
if os.path.isfile(manpath):
    os.remove(manpath)
