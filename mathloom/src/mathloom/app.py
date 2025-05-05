"""
An app to turn natural language into mathematical animations.
"""

from typing import Self
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from mainim.mvp import generate_video

class Mathloom(toga.App):
    def startup(self: Self) -> None:
        main_box: toga.Box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        animation_input_box: toga.Box = toga.Box(style=Pack(direction=COLUMN, padding_bottom=10))

        animation_label: toga.Label = toga.Label(
            text="Describe your math animation in words: ",
            style=Pack(padding_bottom=5)
        )
        self.animation_input: toga.MultilineTextInput = toga.MultilineTextInput(
            placeholder="Write your content here",
            style=Pack(
                flex=1, # Allows the widget to vertically grow
            )
        )
        animation_submit_button: toga.Button = toga.Button("Submit", on_press=self.create_video)

        animation_input_box.add(animation_label, self.animation_input, animation_submit_button)
        main_box.add(animation_input_box)

        self.main_window: toga.MainWindow = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def create_video(self: Self, _) -> None:
        print(self.animation_input.value)

def main() -> Mathloom:
    return Mathloom()
