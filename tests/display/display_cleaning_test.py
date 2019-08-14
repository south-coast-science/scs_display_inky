#!/usr/bin/env python3

"""
Created on 22 Jul 2019
"""

from PIL import ImageFont

from scs_display.display.display import Display


# --------------------------------------------------------------------------------------------------------------------

display = Display(ImageFont.load_default())

display.clean()
