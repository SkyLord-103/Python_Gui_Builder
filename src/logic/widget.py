from property_parser import Parser, ObjParser
import customtkinter as ct
from uuid import uuid4
from rich.console import Console

console = Console()


class Widget:
    """An object to ease gui creation

    Funcs:
        mount: Creates the Widget and its children.
        unmount: Destroys the Widget.
        addChild (Widget): Adds a child to the Widget.
        removeChild (name: str): Name of the child.
        place_configure (*args, **kwargs): Configure the placment of the gui element.
    """
    name = ""
    ctkObject = None
    element = None  # CTkObject
    children = {}
    _props = {}

    def __init__(self, ctkObject, name: str = str(uuid4()), creationArgs: dict = None, addedChildren: list["Widget"] = None, **properties) -> "Widget":
        """Parses properties then makes the gui

        Args:
            ctkObject (any): Any customtkinter object.
            name (str, optional): The name to be put into a child list
            children (dict[str, Widget], optional): Children to belong to this Widget. Defaults to None.
            creationArgs (dict, optional): Options for the gui elment creation to override **properties. Defaults to None.

        Returns:
            Widget: An object to ease gui creation
        """
        self.name = name
        self.ctkObject = ObjParser(ctkObject)
        self._props = Parser(properties)

        if creationArgs is not None:
            self._props.creation = creationArgs

        if addedChildren is not None:
            for _wig in addedChildren:
                self.addChild(_wig)

    def place_configure(self, *args, **kwargs):
        if self.element:
            self.element.place_configure(*args, **kwargs)

    def setparent(self, _widget: any):
        """Set the parent of the widget

        Args:
            _widget (Widget, CTkObject): The widget or customtkinter widget.
        """
        if isinstance(_widget, Widget):
            if _widget.element:
                self._props.creation["master"] = _widget.element
        else:
            self._props.creation["master"] = _widget

    def child(self, name: str) -> any:
        """Returns the child if exists"""
        return self.children.get(name)

    def addChild(self, _widget: any):
        """Adds a child to the widget"""
        console.log("addChild#1", _widget.name, _widget.children,
                    _widget._props.creation["master"], self.name)
        self.children[_widget.name] = {"name": _widget.name}
        console.log("addChild#2", _widget.name, _widget.children,
                    _widget._props.creation["master"], self.name)

        # code that is supposed to work just I get recursion of children
        self.children[_widget.name] = _widget

    def removeChild(self, name: str):
        """Removes a child"""

        _widget = self.children.pop(name)
        if _widget and self.element:
            _widget.unmount()

    def mount(self):
        """Creates every child under this widget.
        Mounting while the gu element is created with redraw it"""
        console.print("WidgetName:", self.name)
        console.print("WidgetElement:", self.element)
        if self.element:
            self.unmount()

        console.print("WidgetProperties:", self._props.creation)
        self.element = self.ctkObject(**self._props.creation)
        self.element.place_configure(**self._props.place)

        # print("Children:", self.children)
        console.print("WidgetChildren:", self.children)
        for name, widge in self.children.items():
            console.print(name, widge)

    def unmount(self):
        """Deletes this gui element"""
        if self.element:
            self.element.destroy()

    def __repr__(self) -> str:
        return f"Widget(name={self.name}, children={self.children})"


if __name__ == "__main__":
    w = ct.CTk()

    button = None

    def cl():
        print("Hello world")

    subbtn = Widget(ct.CTkButton, name="subBtn", master=w, text="CLICK", command=cl, relx=0.3,
                    rely=0.3, relwidth=0.3, relheight=0.4)

    button = Widget(ct.CTkButton, name="MainButton", addedChildren=[
        subbtn
    ], master=w, text="string", relx=0.1,
        rely=0.1, relwidth=0.8, relheight=0.8, command=lambda: print("Hello")).mount()

    # ,
    # widget(ct.CTkButton, name="sbbutton", master=w, text="CLICK", command=cl, relx=0.45,
    #    rely=0.3, relwidth=0.3, relheight=0.4)
    w.mainloop()

# Builder.createWidget("Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5}, [
#     Builder.createWidget(
#         "Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5})
# ]).mount().unmount()
