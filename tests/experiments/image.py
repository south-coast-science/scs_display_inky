#!/usr/bin/env python3

"""
Created on 25 Jan 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://www.raspberrypi.org/forums/viewtopic.php?t=203775
https://stackoverflow.com/questions/54200850/attributeerror-tuple-object-has-no-attribute-type-upon-importing-tensorflow
https://www.cufonfonts.com/font/helvetica-2
"""

import time

from PIL import Image

from inky import InkyPHAT


# --------------------------------------------------------------------------------------------------------------------

colour = "black"            # yellow

print("image...")

inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.WHITE)

img = Image.open("resources/scs_logo_square_inky.png")

start_time = time.time()

inky_display.set_image(img)
inky_display.show()

elapsed_time = time.time() - start_time
print("elapsed: %0.3f" % elapsed_time)
