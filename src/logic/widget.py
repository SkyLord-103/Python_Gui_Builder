from property_parser import Parser, ObjParser
import customtkinter as ct
from uuid import uuid4


class widget:
    """An object to ease gui creation

    Funcs:
        mount: Creates the widget and its children.
        unmount: Destroys the widget.
        addChild (widget): Adds a child to the widget.
        removeChild (name: str): Name of the child.
        place_configure (*args, **kwargs): Configure the placment of the gui element.

    """
    name = ""
    ctkObject = None
    element = None  # CTkObject
    children = {}

    def __init__(self, ctkObject, name: str = "", creationArgs: dict = None, children: list["widget"] = [], **properties) -> "widget":
        """Parses properties then makes the gui

        Args:
            ctkObject (any): Any customtkinter object.
            name (str, optional): The name to be put into a child list
            children (dict[str, widget], optional): Children to belong to this widget. Defaults to None.
            creationArgs (dict, optional): Options for the gui elment creation to override **properties. Defaults to None.

        Returns:
            widget: An object to ease gui creation
        """

        self.ctkObject: ct.CTkButton = ObjParser(ctkObject)
        self._props = Parser(properties)
        if creationArgs:
            self._props.creation = creationArgs

        for _w in children:
            self.addChild(_w)

    def place_configure(self, *args, **kwargs):
        if self.element:
            widget.place_configure(*args, **kwargs)

    def addChild(self, widget: "widget"):
        """Adds a child to the widget"""
        if not widget.name:
            widget.name = uuid4()

        self.children[widget.name] = widget
        if self.element:
            widget.mount()

    def removeChild(self, child: str):
        """Removes a child"""

        _widget = self.children.get(child)
        if _widget and self.element:
            _widget.unmount()

    def mount(self):
        """Creates every child under this widget.
        Mounting while the gu element is created with redraw it"""

        if self.element:
            self.unmount()

        self.element = self.ctkObject(**self._props.creation)
        self.element.place_configure(**self._props.place)

        for _widget in self.children.values():
            _widget.mount()

    def unmount(self):
        """Deletes this gui element"""
        if self.element:
            self.element.destroy()


w = ct.CTk()


button = widget(ct.CTkButton, children=[], master=w, text="string", relx=0.1,
                rely=0.1, relwidth=0.8, relheight=0.8, command=lambda: print("Hello")).mount()


w.mainloop()


# Builder.createWidget("Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5}, [
#     Builder.createWidget(
#         "Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5})
# ]).mount().unmount()
