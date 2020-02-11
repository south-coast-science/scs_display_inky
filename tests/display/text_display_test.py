#!/usr/bin/env python3

"""
Created on 20 Jun 2019
"""

from PIL import ImageFont

from scs_core.data.datetime import LocalizedDatetime

from scs_display.display.text_display import TextDisplay


# --------------------------------------------------------------------------------------------------------------------

now = LocalizedDatetime.now()
date_time = now.as_iso8601()

tzinfo = now.tzinfo
print(tzinfo.fromutc(now.datetime))

display = TextDisplay(ImageFont.load_default())
print(display)
print("-")

display.set_text(0, "SCS Praxis/Handheld v1.0", True)
display.set_text(1, date_time, True)
display.set_text(2, "")
display.set_text(3, "  tag: scs-ap1-6")
display.set_text(4, " host: scs-rpi-006")
display.set_text(5, "")
display.set_text(6, " eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500")
display.set_text(7, "wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500")
display.set_text(8, "")
display.set_text(9, "RUNNING", True)

print(display)
print("-")

display.print_buffer()
print("-")

print("render...")
display.render()
print("-")

print("render...")
display.render()
print("-")


