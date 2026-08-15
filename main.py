from kivy.app import App
from kivy.uix.label import Label


class NEXORAApp(App):
    def build(self):
        return Label(
            text="NEXORA\nAPK is working!",
            font_size="28sp"
        )


if __name__ == "__main__":
    NEXORAApp().run()
