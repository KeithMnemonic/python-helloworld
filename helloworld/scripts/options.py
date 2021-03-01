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


import click


#
# Shared options used my multiple helloworld commands
#
shared_options = {
    "debug": click.option(
        '--debug/--no-debug',
        default=False,
        help="Enable debug logging for the helloworld cli. If unspecified, the"
        " default level 'INFO' will be used."
    ),
    "logfile": click.option(
        '--logfile',
        type=click.Path(writable=True),
        default=None,
        help='File name where the helloworld log will be written.'
    ),
}

#
# custom message options
#
create_options = [
    click.option(
        '-m',
        '--message',
        type=click.STRING,
        required=True,
        help='The custom message to be printed'
    ),
    click.option(
        '-o',
        '--output_file',
        type=click.Path(writable=True),
        default='-',
        help='File name where the message will be written.'
    ),
    shared_options["debug"],
    shared_options["logfile"],
    click.option(
        '--date/--no-date',
        default=False,
        help='Add a date timestamp to the message'
    ),
    click.option(
        '--random/--no-date',
        default=False,
        help='Add a random number to the message'
    ),
    click.option(
        '--clobber/--no-clobber',
        is_flag=True,
        required=False,
        default=False,
        help='If writing output to a file, refuse overwrite an existing file '
        'unless the --clobber option is specified.'
    )
]
