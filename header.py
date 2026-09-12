from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button

class Header(Container):
    def compose(self) -> ComposeResult:
        yield Button("balance...", id="balance_button")
        yield Button("Button2", id="right_button")

    def get_button(self, id):
        button_id = "#"+id
        button = self.query_one(button_id, Button)
        return button
