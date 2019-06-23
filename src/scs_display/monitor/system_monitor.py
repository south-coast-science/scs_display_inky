"""
Created on 21 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

# import sys

from collections import OrderedDict
from multiprocessing import Manager

from scs_core.data.json import JSONable

from scs_core.sync.interval_timer import IntervalTimer
from scs_core.sync.synchronised_process import SynchronisedProcess

from scs_display.display.system_display import SystemDisplay


# --------------------------------------------------------------------------------------------------------------------

class SystemMonitor(SynchronisedProcess):
    """
    classdocs
    """

    UPDATE_INTERVAL =       1.0       # seconds


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, device_name, startup_message, shutdown_message):
        display = SystemDisplay.construct(device_name, startup_message)

        return cls(display, shutdown_message)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, display, shutdown_message):
        """
        Constructor
        """
        manager = Manager()

        SynchronisedProcess.__init__(self, manager.list())

        self.__shutdown_message = shutdown_message
        self.__display = display


    # ----------------------------------------------------------------------------------------------------------------
    # SynchronisedProcess implementation...

    def stop(self):
        # print("SystemMonitor: stop", file=sys.stderr)
        # sys.stderr.flush()

        self.__display.status = self.__shutdown_message
        self.__display.clear()

        super().stop()


    def run(self):
        # print("SystemMonitor: run", file=sys.stderr)
        # sys.stderr.flush()

        try:
            timer = IntervalTimer(self.UPDATE_INTERVAL)

            while timer.true():
                with self._lock:
                    value = self._value

                status = SystemStatus.construct_from_jdict(OrderedDict(value))

                if status is not None:
                    self.__display.status = status.message

                self.__display.update()

        except KeyboardInterrupt:
            pass


    # ----------------------------------------------------------------------------------------------------------------
    # setter for client process...

    def set_message(self, message):
        status = SystemStatus(message)

        if status.is_valid():
            with self._lock:
                status.as_list(self._value)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SystemMonitor:{value:%s, shutdown_message: %s, display:%s}" % \
               (self._value, self.__shutdown_message, self.__display)


# --------------------------------------------------------------------------------------------------------------------

class SystemStatus(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        message = jdict.get('message')

        return SystemStatus(message)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, message):
        """
        Constructor
        """
        self.__message = message                # string


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        return self.message is not None


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['message'] = self.message

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def message(self):
        return self.__message


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SystemStatus:{message:%s}" % self.message
