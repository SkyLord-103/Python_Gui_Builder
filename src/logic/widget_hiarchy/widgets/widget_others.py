from .widget_base import WidgetBase
import customtkinter as _ctk


class OptionMenu(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class CheckBox(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class ComboBox(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Textbox(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Button(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Canvas(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Slider(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Switch(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Frame(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Label(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)


class Entry(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)
