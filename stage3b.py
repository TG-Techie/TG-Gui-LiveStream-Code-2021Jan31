# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# See the file in the root directory of this project for the full licsense text

from tg_gui_std.all import *
import tg_gui_pyportal as setup


@setup.appwrapper
class Application(Layout):

    some_data = State(0.5)

    # now let's make the lable show the value of the slider
    our_label = Label(
        text=DerivedState(some_data, lambda d: f"value: {round(d*100, 2)}")
    )

    our_slider = Slider(value=some_data)

    def _any_(self):
        our_label = self.our_label(top, (self.width, self.height // 2))
        our_slider = self.our_slider(bottom, (9 * self.width // 10, self.height // 2))


setup.run_app_loop()
