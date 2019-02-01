#!/usr/bin/env python3

"""
Created on 25 Jan 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://github.com/simonbugler/inkyphat

https://stackoverflow.com/questions/23734318/fails-to-run-a-simple-pillow-example-cant-find-arial-pil

https://www.raspberrypi.org/forums/viewtopic.php?t=203775
https://stackoverflow.com/questions/54200850/attributeerror-tuple-object-has-no-attribute-type-upon-importing-tensorflow
https://www.cufonfonts.com/font/helvetica-2
"""

import time

from PIL import Image, ImageFont, ImageDraw

from inky import InkyPHAT


# --------------------------------------------------------------------------------------------------------------------

colour = "black"            # yellow

print("hello world...")

inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.BLACK)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('fonts/FredokaOne-Regular.ttf', 24)
# font = ImageFont.load_default()

print("font: %s" % font)

message = "Hello, world!"
w, h = font.getsize(message)

print("w: %d, h:%d" % (w, h))

x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.BLACK, font)

start_time = time.time()

inky_display.set_image(img)
inky_display.show()

elapsed_time = time.time() - start_time
print("elapsed: %0.3f" % elapsed_time)
