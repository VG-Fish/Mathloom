"""
An app to turn natural language into mathematical animations.
"""

from typing import Literal, Self
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from mainim.mvp import generate_video


class Mathloom(toga.App):
    def startup(self: Self) -> None:
        main_box: toga.Box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        animation_input_box: toga.Box = toga.Box(
            style=Pack(direction=COLUMN, padding_bottom=10)
        )

        self.animation_original_text: Literal[
            "Describe your math animation in words: "
        ] = "Describe your math animation in words: "

        self.animation_label: toga.Label = toga.Label(
            text=self.animation_original_text, style=Pack(padding_bottom=5)
        )
        self.animation_input: toga.MultilineTextInput = toga.MultilineTextInput(
            placeholder="Write your content here",
            style=Pack(
                flex=1,  # Allows the widget to vertically grow
            ),
        )
        self.animation_submit_button: toga.Button = toga.Button(
            "Submit", on_press=self.create_video
        )

        animation_input_box.add(
            self.animation_label, self.animation_input, self.animation_submit_button
        )
        main_box.add(animation_input_box)

        self.main_window: toga.MainWindow = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def create_video(self: Self, _) -> None:
        self.process_video_state()

        try:
            await generate_video(self.animation_input.value)
        except Exception as e:
            self.animation_label.text = f"Error: {e}."
        finally:
            self.reset_state()
        
    def process_video_state(self: Self) -> None:
        self.animation_submit_button.enabled = False
        self.animation_label.text = "Processing input..."
    
    def reset_state(self: Self) -> None:
        self.animation_submit_button.enabled = True
        self.animation_label.text = self.animation_original_text
        self.animation_input.value = ""


def main() -> Mathloom:
    return Mathloom()
