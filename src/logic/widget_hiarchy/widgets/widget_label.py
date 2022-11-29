from .widget_base import WidgetBase
import customtkinter as _ctk


class Label(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        super().__init__(_ctk.CTkLabel, name, properties, children)

    def mount(self):
        super().mount()
        self._justify()
