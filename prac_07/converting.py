from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    """ConvertMilesToKilometresApp is a Kivy app for converting miles to kilometres."""
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('converting.kv')
        return self.root

    def handle_convert(self, value_to_check):
        value = self.validate_input_value(value_to_check)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = "{:.2f}".format(result)

    def handle_increment(self, value, increment):
        value = self.validate_input_value(value)
        new_value = float(value) + increment
        self.root.ids.input_number.text = str(new_value)

    def validate_input_value(self, value):
        try:
            validated_value = float(value)
            return validated_value
        except ValueError:
            return 0


ConvertMilesToKilometresApp().run()
