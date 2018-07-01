#!/usr/bin/env python3

import setuptools

setuptools.setup(
    author='Aramís Concepción Durán',
    description='A text-based note-taking application',
    entry_points='[console_scripts]\ntv3=terminal_velocity:main\n',
    install_requires=['urwid==1.1.1', 'chardet==2.1.1'],
    license='GNU General Public License, Version 3',
    long_description=open('README.md').read(),
    name='tv3',
    package_dir={'': 'src'},
    py_modules=['terminal_velocity'],
    url='github.com/aramiscd/tv3',
    version='0.1',
)
