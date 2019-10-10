"""
Created on 20 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys

from scs_display.display.display import Display


# --------------------------------------------------------------------------------------------------------------------

class TextDisplay(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def __print(buffer, file):
        for row in range(len(buffer)):
            print(buffer[row], file=file)

        file.flush()


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, font):
        """
        Constructor
        """
        self.__display = Display(font)

        self.__buffer = [''] * self.text_height
        self.__screen = [''] * self.text_height


    # ----------------------------------------------------------------------------------------------------------------

    def set_text(self, row, text, right_justify=False):
        if not 0 <= row < self.text_height:
            raise ValueError("row out of range: %s" % row)

        if right_justify:
            text = ("%" + str(self.text_width) + "s") % text

        self.__buffer[row] = text[:self.text_width]


    # ----------------------------------------------------------------------------------------------------------------

    def clean(self):
        self.__display.clean()


    def render(self):
        print("TextDisplay.render 1", file=sys.stderr)
        sys.stderr.flush()

        if self.__buffer == self.__screen:
            return False

        print("TextDisplay.render 2", file=sys.stderr)
        sys.stderr.flush()

        for row in range(self.text_height):
            self.__screen[row] = self.__buffer[row]

        self.__display.clear()                          # TODO: try using full-length strings and not clearing
        self.__display.draw_text(self.__screen)
        self.__display.render()

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def text_width(self):
        return self.__display.text_width


    @property
    def text_height(self):
        return self.__display.text_height


    # ----------------------------------------------------------------------------------------------------------------

    def print_buffer(self, file=sys.stdout):
        self.__print(self.__buffer, file)
        file.flush()


    def print_screen(self, file=sys.stdout):
        self.__print(self.__screen, file)
        file.flush()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "TextDisplay:{display:%s, buffer:%s, screen:%s}" % \
               (self.__display, self.__buffer, self.__screen)
