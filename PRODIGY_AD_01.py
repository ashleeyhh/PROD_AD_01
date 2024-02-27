from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        self.expression = ''
        layout = GridLayout(cols=4, spacing=10)
        
        self.result = TextInput(multiline=False, readonly=True, font_size=40)
        layout.add_widget(self.result)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button in buttons:
            if button == '=':
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.calculate)
            elif button == 'C':
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.clear)
            else:
                btn = Button(text=button, font_size=40)
                btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        if instance.text == 'C':
            self.expression = ''
        else:
            self.expression += instance.text
        self.result.text = self.expression

    def calculate(self, instance):
        try:
            self.result.text = str(eval(self.expression))
        except Exception as e:
            self.result.text = "Error"

    def clear(self, instance):
        self.result.text = ''
        self.expression = ''


if __name__ == '__main__':
    CalculatorApp().run()


