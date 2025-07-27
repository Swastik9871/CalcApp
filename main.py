from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class TouchpadCalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Text input for display
        self.solution = TextInput(
            readonly=True,
            font_size=48,
            background_color=[0.1, 0.1, 0.1, 1],
            foreground_color=[1, 1, 1, 1],
            halign="right",
            size_hint=(1, 0.3),
        )
        main_layout.add_widget(self.solution)

        # Button layout
        button_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.7))

        # Buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "Clear", "+",
            "(", ")", "^", "=",
        ]

        for button in buttons:
            if button == "=":
                btn = Button(
                    text=button,
                    font_size=36,
                    background_color=[0.2, 0.8, 0.2, 1],
                    on_press=self.on_solution,
                )
            elif button == "Clear":
                btn = Button(
                    text=button,
                    font_size=36,
                    background_color=[0.8, 0.2, 0.2, 1],
                    on_press=self.clear_solution,
                )
            else:
                btn = Button(
                    text=button,
                    font_size=36,
                    background_color=[0.2, 0.2, 0.2, 1],
                    color=[1, 1, 1, 1],
                    on_press=self.add_to_solution,
                )
            button_layout.add_widget(btn)

        main_layout.add_widget(button_layout)
        return main_layout

    def add_to_solution(self, instance):
        self.solution.text += instance.text

    def clear_solution(self, instance):
        self.solution.text = ""

    def on_solution(self, instance):
        try:
            self.solution.text = str(eval(self.solution.text.replace("^", "**")))
        except Exception:
            self.solution.text = "Error"


if __name__ == "__main__":
    TouchpadCalculatorApp().run()