import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image



class MyApp(App):
    def build(self):
        # Create a root widget
        root = BoxLayout(orientation='vertical',padding=dp(20), spacing=dp(10))
        # Set the title and icon for the app window
        self.title = 'Buy&Sell'
        self.icon = 'my_icon.png'

        # Set the background color
        Window.clearcolor = get_color_from_hex("#FFFFFF")
        Window.size = (360, 640)
            
        # Create a title label and add it to the root widget
        title_label = Label(text='Buy&Sell', font_size=dp(20), size_hint=(1, 0.2),
                            valign='middle', halign='center', bold=True,)
        root.add_widget(title_label)

        image_logo = Image(source="Logo.png.png", size_hint=(
            0, 0), width=95, height=220, pos_hint={"center_x": 0.5, "center_y": 0.5})
        root.add_widget(image_logo)

        # Create a box layout for the input fields
        inputs_layout = BoxLayout(
            orientation='vertical', spacing=dp(10),   size_hint=(1, 0.5))

        # Create text input fields for customer info and add them to the input fields layout
        customer_name_input = TextInput(hint_text='Name', size_hint=(1, None), height=dp(50),multiline=False,
                                        background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(customer_name_input)

        father_name_input = TextInput(hint_text='Father Name', size_hint=(1, None), height=dp(50),multiline=False,
                                      background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(father_name_input)

        id_card_input = TextInput(hint_text='ID Card Number', size_hint=(1, None), height=dp(50),multiline=False,
                                  background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(id_card_input)

        mobile_input = TextInput(hint_text='Mobile Number', size_hint=(1, None), height=dp(50),multiline=False,
                                 background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(mobile_input)

        address_input = TextInput(hint_text='Address', size_hint=(1, None), height=dp(50),multiline=False,
                                  background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(address_input)

        IMEI_input = TextInput(hint_text='IMEI_1', size_hint=(1, None), height=dp(50),multiline=False,
                               background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(IMEI_input)
        IMEI_input = TextInput(hint_text='IMEI_2', size_hint=(1, None), height=dp(50),multiline=False,
                               background_color=get_color_from_hex('#FFFFFF'), foreground_color=get_color_from_hex('#000000'))
        inputs_layout.add_widget(IMEI_input)

        # Add the input fields layout to the root widget
        root.add_widget(inputs_layout)
        root.add_widget(submit_button)
        return root
        # Create a submit button and add it to the root widget


class SubmitButton(Button):
    def __init__(self, **kwargs):
        super(SubmitButton, self).__init__(**kwargs)
        self.text = 'Submit'
        self.font_size = dp(0)
        self.size_hint = (1, 0.1)
        self.height = dp(50)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (1, 0.07, 0.05, 1)  # red color
        self.disabled = False
        self.bold=True

if __name__ == '__main__':
    submit_button = SubmitButton()
    MyApp().run()
