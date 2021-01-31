# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# See the file in the root directory of this project for the full licsense text

# tg_gui_std is a set of common, useful widgets
from tg_gui_std.all import *

# tg_gui_pyportal is some pre-written code to make setting up the pyportal easier
import tg_gui_pyportal as setup

# Any TG-Gui interface is composed of widgets.
# These can be visual widgets like buttons, rectangles, and text or
#   container widgets that group and organize other widgets together.

# an "App" in TG-Gui is written as a class
@setup.appwrapper  # pass it to setup to tell this is the app we want to run
class Application(Layout):

    # first we declare what widgets we want in our app
    our_rect = Rect(fill=color.red)

    # then we delare where we want them
    def _any_(self):
        self.our_rect(
            # 1st argument is a (horizontal, vertical) tuple for poition
            (center, top),
            # 2nd argument is a (horizontal, vertical) tuple for dimensions
            (self.width // 2, self.height // 2),
        )


# lastly run the app
setup.run_app_loop()
