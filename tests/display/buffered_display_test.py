#!/usr/bin/env python3

"""
Created on 20 Jun 2019
"""

from PIL import ImageFont

from scs_display.display.buffered_display import BufferedDisplay


# --------------------------------------------------------------------------------------------------------------------

display = BufferedDisplay(ImageFont.load_default())
print(display)
print("-")

display.set_row(0, "SCS Praxis/Handheld v1.0", True)
display.set_row(1, "")
display.set_row(2, "Thu 20 Jun 14:19:48 BST 2019", True)
display.set_row(3, "")
display.set_row(4, "hostname: scs-rpi-006")
display.set_row(5, "")
display.set_row(6, "    eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500")
display.set_row(7, "   wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500")
display.set_row(8, "")
display.set_row(9, "RUNNING", True)

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

