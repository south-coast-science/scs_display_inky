"""
Created on 20 Jun 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from PIL import Image, ImageDraw

from inky import InkyPHAT


# --------------------------------------------------------------------------------------------------------------------

class Display(object):
    """
    classdocs
    """

    COLOUR =        "black"

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, font):
        """
        Constructor
        """
        self.__font = font

        self.__device = InkyPHAT(self.COLOUR)

        self.__image = Image.new("P", (self.__device.WIDTH, self.__device.HEIGHT))
        self.__surface = ImageDraw.Draw(self.__image)

        m_width, m_height = self.__font.getsize("M")

        self.__text_width = self.__device.WIDTH // m_width
        self.__text_height = self.__device.HEIGHT // m_height + 1


    # ----------------------------------------------------------------------------------------------------------------

    def draw_text(self, buffer):
        for row in range(len(buffer)):
            y_offset = row * self.__text_height
            self.__surface.text((0, y_offset), buffer[row], self.__device.BLACK, self.__font)


    def render(self):
        self.__device.set_image(self.__image)
        self.__device.show()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def text_width(self):
        return self.__text_width


    @property
    def text_height(self):
        return self.__text_height


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Display:{text_width:%s, text_height:%s colour:%s}" % \
               (self.text_width, self.text_height, self.COLOUR)
