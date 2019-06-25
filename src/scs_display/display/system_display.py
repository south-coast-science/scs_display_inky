"""
Created on 21 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys

from PIL import ImageFont

from scs_core.data.localized_datetime import LocalizedDatetime, ISO8601
from scs_core.sys.system_id import SystemID

from scs_display.display.text_display import TextDisplay

from scs_host.sys.host import Host
from scs_host.sys.hostname import Hostname
from scs_host.sys.nmcli import NMCLi


# --------------------------------------------------------------------------------------------------------------------

class SystemDisplay(object):
    """
    classdocs
    """

    __FONT = ImageFont.load_default()

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def system_tag(cls):
        id = SystemID.load(Host)

        return id.message_tag()


    @classmethod
    def system_hostname(cls):
        hostname = Hostname.find()

        return hostname.operational


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, device_name, status):
        datetime = LocalizedDatetime.now()

        tag = cls.system_tag()
        host = cls.system_hostname()

        nmcli = NMCLi.find()
        homes = {} if nmcli is None else nmcli.connections

        return cls(device_name, datetime, tag, host, homes, status)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, device_name, datetime, tag, host, homes, status):
        """
        Constructor
        """
        self.__device_name = device_name                # string
        self.__datetime = datetime                      # string
        self.__tag = tag                                # string
        self.__host = host                              # string
        self.__homes = homes                            # dict of port: network
        self.__status = status                          # string

        self.__display = TextDisplay(self.__FONT)


    # ----------------------------------------------------------------------------------------------------------------

    def update(self):
        self.__datetime = LocalizedDatetime.now()

        nmcli = NMCLi.find()

        if nmcli is not None:
            self.__homes = nmcli.connections

        return self.render()


    def clear(self):
        self.__datetime = None

        self.__homes = {}

        return self.render()


    def render(self):
        self.__display.set_text(0, self.__device_name, True)
        self.__display.set_text(1, self.formatted_datetime, True)
        self.__display.set_text(2, "")
        self.__display.set_text(3, "  tag: %s" % self.__tag)
        self.__display.set_text(4, " host: %s" % self.__host)
        self.__display.set_text(5, "")

        self.__display.set_text(6, "")
        self.__display.set_text(7, "")

        count = 0

        for port, network in self.__homes.items():
            self.__display.set_text(6 + count, "%5s: %s" % (port, network))

            count += 1
            if count > 1:
                break

        self.__display.set_text(8, "")
        self.__display.set_text(9, self.__status, True)

        return self.__display.render()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def status(self):
        return self.__status


    @status.setter
    def status(self, status):
        self.__status = status


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def formatted_datetime(self):
        if self.__datetime is None:
            return ""

        iso = ISO8601.construct(self.__datetime)

        return "%s %s %s" % (iso.date, iso.time, iso.timezone)


    def print(self, file=sys.stdout):
        self.__display.print_buffer(file)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SystemDisplay:{device_name:%s, datetime:%s, tag:%s, host:%s, homes:%s, status:%s, " \
               "display:%s}" % \
               (self.__device_name, self.__datetime, self.__tag, self.__host, self.__homes, self.__status,
                self.__display)
