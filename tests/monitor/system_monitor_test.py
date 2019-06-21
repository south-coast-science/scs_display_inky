#!/usr/bin/env python3

"""
Created on 21 Jun 2019
"""

import sys

from scs_display.monitor.system_monitor import SystemMonitor, SystemStatus


# --------------------------------------------------------------------------------------------------------------------

model = "SCS Praxis/Handheld v1.0"
startup_message = "STARTING"
shutdown_message = "STANDBY"

monitor = SystemMonitor.construct(model, startup_message, shutdown_message)
print(monitor)
print("-")

try:
    monitor.start()

    for line in sys.stdin:
        message = line.strip()

        monitor.set_status(SystemStatus(message))
        print(monitor)

except KeyboardInterrupt:
    pass

finally:
    monitor.stop()

