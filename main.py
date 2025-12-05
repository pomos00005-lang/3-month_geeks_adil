import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'

    greeting_text = ft.Text(value='Hello world!')

    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} hello {name}'
            greeting_text.color = None
            name_input.value = None
        else:
            greeting_text.value = 'Введите корректное имя!'
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label='Enter your name', on_submit=on_button_click)
    button = ft.ElevatedButton(text='Send', on_click=on_button_click)

    page.add(greeting_text, name_input, button)

ft.app(target=main)
