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


import logging
import pathlib
import sys

from helloworld.errors import OutputFileExists

_logger = logging.getLogger(__name__)


def write_message(message, output_file, clobber=False):
    if output_file != '-':
        # only overwrite output_file if --clobber specified.
        if pathlib.Path(output_file).exists() and not clobber:
            raise OutputFileExists(output_file)

        _logger.debug("Writing message to %s",
                      output_file)
        with open(output_file, "w") as _outfile:
            _outfile.write(message)
    else:
        _logger.debug("Writing message to stdout")
        sys.stdout.write(message + "\n")


def create_logger(level='INFO', logfile=None):
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level, None))

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s'
                                  ' - %(message)s')
    if logfile:
        lh = logging.FileHandler(logfile, mode='w')
    else:
        lh = logging.StreamHandler()

    lh.setLevel(getattr(logging, level, None))
    lh.setFormatter(formatter)
    logger.addHandler(lh)

    return logger
