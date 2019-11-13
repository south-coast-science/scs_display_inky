#!/usr/bin/env python3

"""
Created on 21 Jun 2019
"""

import time

from scs_display.display.system_display import SystemDisplay


# --------------------------------------------------------------------------------------------------------------------

queue_report_filename = '/tmp/southcoastscience/mqtt_queue_report.json'
gps_report_filename = '/tmp/southcoastscience/gps_report.json'

model = "SCS Praxis/Handheld v1.0"
status_message = "RUNNING"

display = SystemDisplay.construct(model, status_message, True, queue_report_filename, gps_report_filename)
print(display)
print("-")

display.render(None, {}, "test")
display.print()
print("-")

try:
    while True:
        time.sleep(5)
        display.update()

except KeyboardInterrupt:
    pass

display.system_status = "STANDBY"
display.clear()
display.print()
print("-")

