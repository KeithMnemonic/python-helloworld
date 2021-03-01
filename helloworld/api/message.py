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
import datetime
from random import randint


_logger = logging.getLogger(__name__)


def create_message(name, date=False, lottery=False):

    _logger.debug("Creating message object")
    doc = HelloWorldMessage(name, date, lottery)

    return doc._message


class HelloWorldMessage:
    """
    Base HelloWorldMessage class.

    """

    def __init__(self, name, date, lottery):
        self._message = (f"Hello {name}, ")
        if date:
            _logger.debug("Add date to message")
            self._date = (f"today is {datetime.datetime.now().strftime('%c')}"
                          f".")
            self._message = self._message + self._date
        if lottery:
            _logger.debug("Add lottery number to message")
            self._lottery = (f" Your lottery number is {randint(1, 1000)}")
            self._message = self._message + self._lottery
