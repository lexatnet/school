# возможность использовать модули написаные другими людьми
# делает разработку приложений более быстрой и простой
# важно хорошо изучить документацию к используемым модулям

# потратив некоторое время для того чтобы выбрать модуль
# мною был выбран модуль python-prompt-toolkit он лучшим образом подходит
# для работы с консолью построения диологов и консольной графики

# лучше всего использовать последнюю версию модуля
# она содержит последние наработки и исправления

# установка модуля
# скачать модкль можно по следующей ссылке https://github.com/jonathanslenders/python-prompt-toolkit/
# если умеете пользоваться git то можно клонировать репозиторий
# если нет
# на странице можно скачать архив содержаший все файлы
# щёлкнув мышкой на кнопке "clone or download" вы увидите меню со ссылкой "download ZIP"
# распаковав архив перейдите в директорию в которой лежат распакованные файлы и
# установите модуль запусив команду `python setup.py install` в распакованной директории модуля
# выполнение этой команды потребует администраторских привелегий
# так что лучше если вы выполните эту команду запустив
# командную строку с администраторскими привелегиями и перейдя в необходимую директорию

# теперь можно использовать модуль
"""
A simple example of a few buttons and click handlers.
"""
from __future__ import unicode_literals
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import VSplit, HSplit, Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Button, Box, TextArea, Label, Frame


# Event handlers for all the buttons.
def button1_clicked():
    text_area.text = 'Button 1 clicked'


def button2_clicked():
    text_area.text = 'Button 2 clicked'


def button3_clicked():
    text_area.text = 'Button 3 clicked'


def exit_clicked():
    get_app().exit()


# All the widgets for the UI.
button1 = Button('Button 1', handler=button1_clicked)
button2 = Button('Button 2', handler=button2_clicked)
button3 = Button('Button 3', handler=button3_clicked)
button4 = Button('Exit', handler=exit_clicked)
text_area = TextArea(focusable=True)


# Combine all the widgets in a UI.
# The `Box` object ensures that padding will be inserted around the containing
# widget. It adapts automatically, unless an explicit `padding` amount is given.
root_container = Box(
    HSplit([
        Label(text='Press `Tab` to move the focus.'),
        VSplit([
            Box(
                body=HSplit(
                    [button1, button2, button3, button4],
                    padding=1),
                padding=1,
                style='class:left-pane'),
            Box(
                body=Frame(text_area),
                padding=1,
                style='class:right-pane'),
        ]),
    ]),
)

layout = Layout(
    container=root_container,
    focused_element=button1)


# Key bindings.
kb = KeyBindings()
kb.add('tab')(focus_next)
kb.add('s-tab')(focus_previous)


# Styling.
style = Style([
    ('left-pane', 'bg:#888800 #000000'),
    ('right-pane',      'bg:#00aa00 #000000'),
    ('button',          '#000000'),
    ('button-arrow',    '#000000'),
    ('button focused', 'bg:#ff0000'),
    ('text-area focused', 'bg:#ff0000'),
])


# Build a main application object.
application = Application(
    layout=layout,
    key_bindings=kb,
    style=style,
    full_screen=True)


def main():
    application.run()


if __name__ == '__main__':
    main()
