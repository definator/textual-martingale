from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button

class Header(Container):
    def compose(self) -> ComposeResult:
        yield Button("balance...", id="balance_button")
        yield Button("Button2", id="right_button")
