from textual.app import App, ComposeResult
from header import Header

class MartingaleApp(App):
    CSS_PATH = "style/header_style.tcss"
    def compose(self) -> ComposeResult:
        yield Header()




if __name__ == "__main__":
    app = MartingaleApp()
    app.run()
