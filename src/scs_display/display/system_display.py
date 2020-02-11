"""
Created on 21 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys

from PIL import ImageFont

from scs_core.data.datetime import LocalizedDatetime, ISO8601
from scs_core.data.queue_report import QueueReport, QueueStatus

from scs_core.position.gps_datum import GPSDatum

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

    __QUEUE_STATE = {
        QueueStatus.NONE:               "FAULT",
        QueueStatus.INHIBITED:          "PUBLISHING INHIBITED",
        QueueStatus.STARTING:           "STARTING",
        QueueStatus.CONNECTING:         "CONNECTING",
        QueueStatus.WAITING_FOR_DATA:   "PREPARING DATA",
        QueueStatus.PUBLISHING:         "PUBLISHING DATA",
        QueueStatus.CLEARING:           "PUBLISHING DATA",
        QueueStatus.QUEUING:            "QUEUING DATA"
    }

    __FONT = ImageFont.load_default()


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def system_tag():
        id = SystemID.load(Host)

        return id.message_tag()


    @staticmethod
    def system_hostname():
        hostname = Hostname.find()

        return hostname.operational


    @staticmethod
    def formatted_datetime(datetime):
        if datetime is None:
            return ""

        iso = ISO8601.construct(datetime)

        if iso is None:
            return ""

        return "%s %s %s" % (iso.date, iso.time, iso.timezone)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, device_name, status_message, show_time, queue_report_filename, gps_report_filename):
        tag = cls.system_tag()
        hostname = cls.system_hostname()

        return cls(device_name, tag, hostname, status_message, show_time,
                   queue_report_filename, gps_report_filename)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, device_name, tag, hostname, status_message, show_time,
                 queue_report_filename, gps_report_filename):
        """
        Constructor
        """
        self.__device_name = device_name                                    # string
        self.__tag = tag                                                    # string
        self.__hostname = hostname                                          # string
        self.__status_message = status_message                              # string
        self.__show_time = show_time                                        # bool

        self.__queue_report_filename = queue_report_filename                # string
        self.__gps_report_filename = gps_report_filename                    # string

        self.__display = TextDisplay(self.__FONT)


    # ----------------------------------------------------------------------------------------------------------------

    def clean(self):
        self.__display.clean()


    def update(self):
        # time...
        display_datetime = self.__show_time and Host.time_is_synchronized()
        datetime = LocalizedDatetime.now() if display_datetime else None

        # network...
        nmcli = NMCLi.find()
        homes = {} if nmcli is None else nmcli.connections

        # message...
        message = self.__status_message

        # MQTT queue...
        if self.__queue_report_filename:
            queue_report = QueueReport.load(self.__queue_report_filename)
            queue_message = self.__QUEUE_STATE[queue_report.queue_state()]

            message += ':' + queue_message

        # GPS quality...
        if self.__gps_report_filename:
            gps_report = GPSDatum.load(self.__gps_report_filename)
            gps_quality = gps_report.quality

            message += '  GPS:' + str(gps_quality)

        return self.render(datetime, homes, message)


    def clear(self):
        return self.render(None, {}, self.__status_message)


    def render(self, datetime, homes, message):
        self.__display.set_text(0, self.__device_name, True)
        self.__display.set_text(1, self.formatted_datetime(datetime), True)
        self.__display.set_text(2, "")
        self.__display.set_text(3, "  tag: %s" % self.__tag)
        self.__display.set_text(4, " host: %s" % self.__hostname)
        self.__display.set_text(5, "")

        self.__display.set_text(6, "")
        self.__display.set_text(7, "")

        count = 0

        for port, network in homes.items():
            self.__display.set_text(6 + count, "%5s: %s" % (port, network))

            count += 1
            if count > 1:
                break

        self.__display.set_text(8, "")
        self.__display.set_text(9, message, True)

        return self.__display.render()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def status_message(self):
        return self.__status_message


    @status_message.setter
    def status_message(self, status_message):
        self.__status_message = status_message


    # ----------------------------------------------------------------------------------------------------------------

    def print(self, file=sys.stdout):
        self.__display.print_buffer(file)


    def __str__(self, *args, **kwargs):
        return "SystemDisplay:{device_name:%s, tag:%s, hostname:%s status_message:%s, show_time:%s, " \
               "queue_report_filename:%s, gps_report_filename:%s, gps_report_filename:%s, display:%s}" % \
               (self.__device_name, self.__tag, self.__hostname, self.__status_message, self.__show_time,
                self.__queue_report_filename, self.__gps_report_filename, self.__gps_report_filename, self.__display)
