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

        self.element = None  # CTkObject
        self.children = {}

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
        self.children[_widget.name] = _widget

    def removeChild(self, name: str):
        """Removes a child"""

        _widget = self.children.pop(name)
        if _widget and self.element:
            _widget.unmount()

    def mount(self):
        """Creates every child under this widget.
        Mounting while the gu element is created with redraw it"""
        if self.element:
            self.unmount()

        self.element = self.ctkObject(**self._props.creation)
        self.element.place_configure(**self._props.place)

        for name, widge in self.children.items():
            widge.setparent(self.element)
            widge.mount()

    def unmount(self):
        """Deletes this gui element"""
        if self.element:
            self.element.destroy()

    def __repr__(self) -> str:
        return f"Widget(name={self.name}, children={self.children})"


if __name__ == "__main__":
    w = ct.CTk()

    button = Widget(ct.CTkButton, name="MainButton", addedChildren=[
        Widget(ct.CTkButton, addedChildren=[
            Widget(ct.CTkButton, name="subBtn", master=w, fg_color="#eab7ff", text="CLICK", relx=0.3,
                    rely=0.3, relwidth=0.3, relheight=0.4)],
               name="subature", master=w, fg_color="#55aa94", text="CLICK", relx=0.3,
               rely=0.3, relwidth=0.3, relheight=0.4)
    ], master=w, text="string", relx=0.1,
        rely=0.1, relwidth=0.8, relheight=0.8).mount()

    console.print(button)
    # console.print(button.child("subBtn"))
    # ,
    # widget(ct.CTkButton, name="sbbutton", master=w, text="CLICK", command=cl, relx=0.45,
    #    rely=0.3, relwidth=0.3, relheight=0.4)
    w.mainloop()

# Builder.createWidget("Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5}, [
#     Builder.createWidget(
#         "Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5})
# ]).mount().unmount()
