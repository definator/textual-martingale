from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button

class Header(Horizontal):
    def compose(self) -> ComposeResult:
        yield Button("Button1", id="left_button")
        yield Button("Button2", id="right_button")
