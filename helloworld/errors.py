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


class HelloWorldError(Exception):
    """
    Base class for errors thrown by python-helloword. Any class inheriting from
    it must implement a `message` attribute at the very least.
    """


class CLIError(HelloWorldError):
    """Base class for CLI errors."""


class OutputFileExists(CLIError):
    """
    Exception raised when trying to overwrite a file without --clobber.

    Attributes:

        message -- the message to be reported to the user.
        output_file -- the output file that already exists.
    """

    def __init__(self, output_file):
        message = (f"Attempted to overwrite existing file '{output_file}' " +
                   "without specifying '--clobber' option.")
        self.output_file = output_file
        super().__init__(message)


class APIError(HelloWorldError):
    """Base class for exceptions thrown by pythoh-helloword
       API.

    Attributes:
        message -- relevant error message
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)
