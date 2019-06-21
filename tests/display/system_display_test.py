#!/usr/bin/env python3

"""
Created on 21 Jun 2019
"""

import time

from scs_display.display.system_display import SystemDisplay


# --------------------------------------------------------------------------------------------------------------------

model = "SCS Praxis/Handheld v1.0"
status = "RUNNING"

display = SystemDisplay.construct(model, status)
print(display)
print("-")

display.render()
display.print()
print("-")

try:
    while True:
        time.sleep(1)
        display.update()

except KeyboardInterrupt:
    pass

display.clear("STANDBY")
display.print()
print("-")

