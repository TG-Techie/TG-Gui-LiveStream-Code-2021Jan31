# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# See the file in the root directory of this project for the full licsense text

from tg_gui_std.all import *
import tg_gui_pyportal as setup


@setup.appwrapper
class Application(Layout):

    # state is a way of managing what data our app displays
    some_data = State(0.5)

    # we'll start with just a slider and some text
    our_label = Label(text="Can You See Me?")
    our_slider = Slider(value=some_data)

    def _any_(self):
        our_label = self.our_label(top, (self.width, self.height // 2))
        our_slider = self.our_slider(bottom, (9 * self.width // 10, self.height // 2))


setup.run_app_loop()
