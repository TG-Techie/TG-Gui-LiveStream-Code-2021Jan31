# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# See the file in the root directory of this project for the full licsense text

from tg_gui_std.all import *
import tg_gui_pyportal as setup


@setup.appwrapper
class Application(Layout):

    # start with three rects and play around with potioning
    rect1 = Rect(fill=color.red)
    rect2 = Rect(fill=color.green)
    rect3 = Rect(fill=color.blue)

    def _any_(self):
        # save the size here to make the code clearer
        rect_size = (self.width // 3, self.height // 3)
        # use `rect1 = self.rects(...)` to make out code clearer
        rect1 = self.rect1((left, top), rect_size)
        # use the position descriptors `above`, `below`, `rightof`, and `leftof` to place widgets
        rect2 = self.rect2(below(rect1), rect_size)
        rect3 = self.rect3(rightof(rect2), rect_size)
        # here we have the sizes as all the same but they don't have to be,
        #   try making rect3's dimentions (self.width // 2, self.height // 3)


setup.run_app_loop()
