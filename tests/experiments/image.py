#!/usr/bin/env python3

"""
Created on 25 Jan 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://www.raspberrypi.org/forums/viewtopic.php?t=203775
https://stackoverflow.com/questions/54200850/attributeerror-tuple-object-has-no-attribute-type-upon-importing-tensorflow
https://www.cufonfonts.com/font/helvetica-2
"""

from PIL import Image

from inky import InkyPHAT


# --------------------------------------------------------------------------------------------------------------------

print("image...")


inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/SCS/scs_display_inky/tests/resources/scs_logo_square_inky.png")

inky_display.set_image(img)
inky_display.show()
