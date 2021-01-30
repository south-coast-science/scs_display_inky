"""
Created on 21 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example JSON:
{"mode": "SYS", "device-name": "SCS Praxis/Handheld (dev)", "startup-message": "ON", "shutdown-message": "STANDBY",
"show-time": true}
"""

from scs_core.display.display_conf import DisplayConf as AbstractDisplayConf

from scs_display.monitor.system_monitor import SystemMonitor


# --------------------------------------------------------------------------------------------------------------------

class DisplayConf(AbstractDisplayConf):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, mode, device_name, startup_message, shutdown_message, show_time):
        """
        Constructor
        """
        super().__init__(mode, device_name, startup_message, shutdown_message, show_time)


    # ----------------------------------------------------------------------------------------------------------------

    def monitor(self, software_report, psu_report_class, psu_report_filename, queue_report_filename,
                gps_report_filename):
        if self.mode == 'SYS':
            device_name = self.device_name + ':' + software_report if software_report else self.device_name

            return SystemMonitor.construct(device_name, self.startup_message, self.shutdown_message, self.show_time,
                                           psu_report_class, psu_report_filename, queue_report_filename,
                                           gps_report_filename)

        raise ValueError('unknown mode: %s' % self.mode)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DisplayConf(display):{mode:%s, device_name:%s, startup_message:%s, shutdown_message:%s, " \
               "show_time:%s}" %  \
               (self.mode, self.device_name, self.startup_message, self.shutdown_message,
                self.show_time)
