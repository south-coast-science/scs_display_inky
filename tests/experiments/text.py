#!/usr/bin/env python3

"""
Created on 20 Jun 2019
"""

import time

from PIL import Image, ImageFont, ImageDraw

from inky import InkyPHAT


# --------------------------------------------------------------------------------------------------------------------

colour = "black"            # yellow

print("text...")

inky_display = InkyPHAT(colour)
# inky_display.set_border(inky_display.BLACK)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()

print("font: %s" % font)

message = "1-123456789-123456789-123456789-123"
w, h = font.getsize(message)

print("w: %d, h:%d" % (w, h))

# x = (inky_display.WIDTH / 2) - (w / 2)
# y = (inky_display.HEIGHT / 2) - (h / 2)

x = 0
y = 0

draw.text((x, y), message, inky_display.BLACK, font)

message = "2-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "3-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "4-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "5-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "6-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "7-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "8-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

message = "9-123456789-123456789-123456789-123"
y += h

draw.text((x, y), message, inky_display.BLACK, font)

start_time = time.time()

inky_display.set_image(img)
inky_display.show()

elapsed_time = time.time() - start_time
print("elapsed: %0.3f" % elapsed_time)
