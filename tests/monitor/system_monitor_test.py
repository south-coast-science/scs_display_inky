#!/usr/bin/env python3

"""
Created on 21 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
"""

import sys

from scs_display.monitor.system_monitor import SystemMonitor, SystemStatus


# --------------------------------------------------------------------------------------------------------------------

queue_report_filename = '/tmp/southcoastscience/mqtt_queue_report.json'
gps_report_filename = '/tmp/southcoastscience/gps_report.json'

model = "SCS Praxis/Handheld v1.0"
startup_message = "STARTING"
shutdown_message = "STANDBY"

monitor = SystemMonitor.construct(model, startup_message, shutdown_message, True,
                                  queue_report_filename, gps_report_filename)
print(monitor)
print("-")

try:
    monitor.start()

    for line in sys.stdin:
        message = line.strip()

        monitor.set_status(SystemStatus(message))

except KeyboardInterrupt:
    pass

finally:
    monitor.stop()

