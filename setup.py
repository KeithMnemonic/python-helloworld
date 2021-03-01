#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Setup script."""

# Copyright (c) 2021 SUSE LLC
#
# This file is part of python-helloworld
#
# python-helloworld is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or # (at your option) any later version.
#
# python-helloworld is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-helloworld.
# If not, see <http://www.gnu.org/licenses/>.


from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as req_file:
    requirements = req_file.read().splitlines()

with open('requirements-test.txt') as req_file:
    test_requirements = req_file.read().splitlines()[2:]

with open('requirements-dev.txt') as req_file:
    dev_requirements = test_requirements + req_file.read().splitlines()[2:]

tox_requirements = [
    'tox',
    'tox-pyenv'
]


setup(
    name='helloworld',
    version='1.0.0',
    description="Package used to demonstrate tips for vscode.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="SUSE",
    author_email='kberger@suse.com',
    url='https://github.com/KeithMnemonic/python-helloworld',
    packages=find_packages(),
    package_dir={
        'helloworld': 'helloworld'
    },
    entry_points={
        'console_scripts': [
            'helloworld=helloworld.scripts.cli:cli'
        ]
    },
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
        'test': test_requirements,
        'tox': tox_requirements
    },
    license='GPLv3+',
    zip_safe=False,
    keywords='helloworld',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
