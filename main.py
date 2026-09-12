import time
from textual.app import App, ComposeResult
from header import Header

class MartingaleApp(App):
    CSS_PATH = "style/header_style.tcss"
    def compose(self) -> ComposeResult:
        self.header = Header()
        yield self.header

    def on_mount(self) -> None:
        self.set_timer(5, self.change_button)

    def change_button(self) -> None:
        balance_button = self.header.get_button("balance_button")
        balance_button.label = "changed but!!!"



if __name__ == "__main__":
    app = MartingaleApp()
    app.run()
