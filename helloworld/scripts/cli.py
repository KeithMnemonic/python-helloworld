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
import sys

import click

import helloworld.scripts.cli_utils as cli_utils
import helloworld.scripts.options as cli_options
from helloworld.errors import CLIError, APIError


def _setup_logger(debug, logfile):
    # Setup root logger
    cli_utils.create_logger(("DEBUG" if debug else "INFO"), logfile)

    # Setup cli logger
    return logging.getLogger(__name__)


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


# default click group
@click.group()
@click.version_option()
def cli():
    """
    The command line is the main interface to python-helloworld.
    """


# Click section for the "update" command
@cli.command()
@add_options(cli_options.create_options)
def custom(message, date, logfile, output_file, debug, clobber):
    """
    Print a custom Hello message.
    """
    # Setup cli logger
    _logger = _setup_logger(debug, logfile)

    _logger.info("Printing Hello message using custom message '%s'", message)

    if date:
        _logger.debug("Add date to message")

    try:
        cli_utils.write_message(message, output_file, clobber)
    except CLIError as e:
        print('ERROR: {}'.format(str(e)), file=sys.stderr)
        if logfile or debug:
            _logger.exception(e)
        sys.exit(1)
    except APIError as e:
        print('ERROR: {}'.format(str(e)), file=sys.stderr)
        if logfile or debug:
            _logger.exception(e)
        sys.exit(1)

    sys.exit(0)
