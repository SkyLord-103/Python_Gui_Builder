from .widget_base import WidgetBase
import customtkinter as _ctk


class Label(WidgetBase):
    def __init__(self, name: str = None, properties=None, children: list = None):
        self._justify_f = properties.ctk.pop("justify", 'c')

        super().__init__(_ctk.CTkLabel, name, properties, children)

        self._justify_positions = {
            'n': (_ctk.N, 0.5, 0),
            's': (_ctk.S, 0.5, 1),
            'w': (_ctk.W, 0, 0.5),
            'e': (_ctk.E, 1, 0.5),
            'c': (_ctk.CENTER, 0.5, 0.5)
        }

    def _justify(self):
        """Internal function, Sets the text_label to the given side"""
        if not self.element:
            return

        just = self._justify_positions[self._justify_f]
        self.element.text_label.place(
            anchor=just[0], relx=just[1], rely=just[2], x=0, y=0)

    def mount(self):
        super().mount()
        self._justify()
