from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Create vertical layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Create text input field
        self.input_field = TextInput(hint_text='Type something here...', font_size=24, multiline=False)
        self.layout.add_widget(self.input_field)

        # Create button
        submit_button = Button(text='Display Text', font_size=24, size_hint=(1, 0.3))
        submit_button.bind(on_press=self.display_text)
        self.layout.add_widget(submit_button)

        # Create label to display typed text
        self.output_label = Label(text='', font_size=28)
        self.layout.add_widget(self.output_label)

        return self.layout

    def display_text(self, instance):
        # Display input field text in the label
        typed_text = self.input_field.text
        self.output_label.text = f"You typed: {typed_text}"

# Run the app
if __name__ == '__main__':
    TextInputApp().run()
