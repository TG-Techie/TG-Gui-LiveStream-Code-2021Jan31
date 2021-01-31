# The MIT License (MIT)
#
# Copyright (c) 2021 Jonah Yolles-Murphy (TG-Techie)
#
# See the file in the root directory of this project for the full licsense text

from tg_gui_std.all import *
import tg_gui_pyportal as setup


@setup.appwrapper
class Application(Layout):

    # inputs from the sliders
    r, g, b = State(0.5), State(0.5), State(0.5)
    # convert the inputs to color
    rgb = DerivedState(
        (r, g, b),
        lambda r, g, b: color.fromfloats(r, g, b),
    )

    # our output
    sample_color = Rect(fill=rgb)
    hexout = Label(text=DerivedState(rgb, lambda rgb: hex(rgb)))

    r_slider = Slider(value=r)
    g_slider = Slider(value=g)
    b_slider = Slider(value=b)

    def _any_(self):

        # +-----------+-----------+
        # | color     | hex       |
        # +-----------+-----------+
        # | red slider            |
        # +-----------------------+
        # | green slider          |
        # +-----------------------+
        # | blue slider           |
        # +-----------------------+

        sample_size = (self.width // 2, self.height // 4)
        sample_color = self.sample_color((left, top), sample_size)
        hexout = self.hexout((right, top), sample_size)

        slider_size = (self.width, self.height // 4)
        r_slider = self.r_slider((center, below(sample_color)), slider_size)
        g_slider = self.g_slider(below(r_slider), slider_size)
        b_slider = self.b_slider(below(g_slider), slider_size)


if __name__ == "__main__":
    setup.run_app_loop()
