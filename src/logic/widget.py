from typing import Optional
from property_parser import WidgetParser, ObjParser
import customtkinter as ct
from uuid import uuid4


class Widget:
    """An object to ease gui creation

    Funcs:
        mount: Creates the Widget and its children.
        unmount: Destroys the Widget.
        addChild (Widget): Adds a child to the Widget.
        removeChild (name: str): Name of the child.
        place_configure (*args, **kwargs): Configure the placment of the gui element.
    """

    def __init__(self, ctkObject, name: str = None, properties=None, creationArgs: Optional[dict] = None, children: list["Widget"] = None) -> "Widget":
        """Parses properties then makes the gui

        Args:
            ctkObject (any): Any customtkinter object.
            name (str, optional): The name to be put into a child list
            properties (namespace(creation, place)): The parsed properties for the widget
            creationArgs (dict, optional): Options for the gui elment creation to override properties. Defaults to None.
            children (dict[str, Widget], optional): Children to belong to this Widget. Defaults to None.

        Returns:
            Widget: An object to ease gui creation
        """
        self._name = ctkObject
        self.name = name or str(uuid4())
        self.ctkObject = ObjParser(ctkObject)

        self.afterCreate = properties.creation.pop("afterCreate", None)
        # properties.creation["anchor"] = properties.creation.pop(
        #     "justify", 'center')
        self._justify_f = properties.creation.pop("justify", 'c')
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

        if creationArgs is not None:
            self._props.creation = creationArgs

        if children is not None:
            for _wig in children:
                self.addChild(_wig)

    @classmethod
    def parse(cls, **properties):
        """Returns parsed properties"""
        return WidgetParser(properties)

    def place_configure(self, *args, **kwargs):
        if self.element:
            self.element.place_configure(*args, **kwargs)

    def _justify(self):
        """Internal function, Sets the text_label to the given side"""
        if not self.element:
            return

        just = self._justify_positions[self._justify_f]
        print("Justing:", self.element.text_label, self.name)
        self.element.text_label.place(
            anchor=just[0], relx=just[1], rely=just[2], x=0, y=0)

    def child(self, name: str) -> any:
        """Returns the child if exists"""
        return self.children.get(name)

    def addChild(self, _widget: any):
        """Adds a child to the widget"""
        if isinstance(_widget, Widget):
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

        self.element = self.ctkObject(**self._props.creation)
        self.element.place_configure(**self._props.place)

        if self.ctkObject.__name__ in ("CTkLabel", "CTkButton"):
            self._justify()

        if self.afterCreate is not None:
            self.afterCreate(self, self.element)

        for widge in self.children.values():
            widge.setparent(self.element)
            widge.mount()

    def unmount(self):
        """Deletes this gui element"""
        if self.element:
            self.element.destroy()

    def __repr__(self) -> str:
        return f"Widget(name={self.name}, children={self.children})"


if __name__ == "__main__":
    window = ct.CTk()
    print("__main__")
    _frame = Widget('CTkFrame', properties=Widget.parse(
        relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9
    ))

    helloButton = Widget('CTkButton', properties=Widget.parse(
        relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9, text="Hello"
    ))

    _frame.addChild()
    _frame.mount()
    window.mainloop()
