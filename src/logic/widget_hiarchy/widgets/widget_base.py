
from typing import Optional

from ..parser import ObjParser
import customtkinter as ct
from uuid import uuid4


class WidgetBase:
    """WidgetBase the base for the widgets"""

    def __init__(self, ctkObject, name: str = None, properties=None, children: list = None):

        self.name = name or str(uuid4())
        self.ctkObject = ObjParser(ctkObject)

        self.afterCreate = properties.ctk.pop("afterCreate", None)

        self._justify_f = properties.ctk.pop("justify", 'c')
        self._justify_positions = {
            'n': (ct.N, 0.5, 0),
            's': (ct.S, 0.5, 1),
            'w': (ct.W, 0, 0.5),
            'e': (ct.E, 1, 0.5),
            'c': (ct.CENTER, 0.5, 0.5)
        }
        self._props = properties

        self.element = None  # CTkObject
        self.children = {}

        if children is not None:
            for _wig in children:
                self.addChild(_wig)

    def configure(self, *args, **kwargs):
        if self.element:
            self.element.configure(*args, **kwargs)

    def place_configure(self, *args, **kwargs):
        if self.element:
            self.element.place_configure(*args, **kwargs)

    def _justify(self):
        """Internal function, Sets the text_label to the given side"""
        if not self.element:
            return

        just = self._justify_positions[self._justify_f]
        self.element.text_label.place(
            anchor=just[0], relx=just[1], rely=just[2], x=0, y=0)

    def setparent(self, _widget: any):
        """Set the parent of the widget

        Args:
            _widget (Widget, Window, CTkObject): The widget, window or customtkinter widget.
        """
        if isinstance(_widget, WidgetBase):
            if _widget.element:
                self._props.creation["master"] = _widget.element
        elif _widget.__class__.__name__ == "Window":
            self._props.creation["master"] = _widget.window
        else:
            self._props.creation["master"] = _widget

    def child(self, name: str) -> any:
        """Returns the child if exists"""
        return self.children.get(name)

    def addChild(self, _widget: any):
        """Adds a child to the widget"""
        if isinstance(_widget, WidgetBase):
            self.children[_widget.name] = _widget
        if isinstance(_widget, list):
            for widge in _widget:
                self.children[widge.name] = widge

    def removeChild(self, name: str):
        """Removes a child"""
        _widget = self.children.pop(name)
        if _widget and self.element:
            _widget.unmount()

    def mount(self):
        """Creates every child under this widget.
        Mounting while the gui element is created will redraw it"""
        if self.element:
            self.unmount()

        self.element = self.ctkObject(**self._props.ctk)
        self.element.place_configure(**self._props.place)

        if self.afterCreate is not None:
            self.afterCreate(self, self.element)

        for widge in self.children.values():
            widge.setparent(self.element)
            widge.mount()

    def unmout(self):
        """Deletes this gui element"""
        if self.element:
            self.element.destroy()
