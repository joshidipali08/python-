#Design Counter App (This app has a button that increments a counter displayed on the screen every time the button is clicked)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        # Create layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Create label to show the count
        self.count = 0
        self.label = Label(text=str(self.count), font_size=72)
        layout.add_widget(self.label)

        # Create button to increment the counter
        button = Button(text='Click Me!', font_size=32, size_hint=(1, 0.4))
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)

        return layout

    def increment_counter(self, instance):
        self.count += 1
        self.label.text = str(self.count)

# Run the app
if __name__ == '__main__':
    CounterApp().run()
