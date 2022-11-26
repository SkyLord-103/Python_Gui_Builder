import uuid
from property_parser import WindowParser, Namespace
from rich.console import Console
import customtkinter as ct
from widget import Widget

console = Console()


class Window:
    """Gui Window

    Funcs:
        mount: Creates the Widget and its children.
        unmount: Destroys the Widget.
        addChild (Widget): Adds a child to the Widget.
        removeChild (name: str): Name of the child.
        configure (*args, **kwargs): Configure the window.
    """

    def __init__(self, name: str = "Window", properties=None, tkinterWindow: bool = False, widgets: list["Widget"] = None) -> "Window":
        """Parses properties then makes the gui

        Args:
            name (str, optional): The name to be put into a child list
            properties (namespace(creation, place)): The parsed properties for the widget
            tkinterWindow (bool, optional): Not implemented.
            widgets (list[Widget], optional): Children to belong to this window. Defaults to None.

        Returns:
            Widget: An object to ease gui creation
        """
        self.name = name
        self._props = properties or Namespace(ctk={}, user={})

        self.window = None
        self.widgets = {}

        if widgets is not None:
            for _wig in widgets:
                self.addChild(_wig)

    @classmethod
    def parse(cls, **properties):
        """Returns parsed properties"""
        return WindowParser(properties)

    def child(self, name: str) -> Widget | None:
        """Returns the child if exists"""
        return self.widgets.get(name)

    def addChild(self, _widget: list | Widget):
        """Adds a child to the window"""
        if isinstance(_widget, Widget):
            self.widgets[_widget.name] = _widget
        if isinstance(_widget, list):
            for widge in _widget:
                self.widgets[widge.name] = widge

    def removeChild(self, name: str):
        """Removes a child"""

        _widget = self.widgets.pop(name)
        if _widget and self.window:
            _widget.unmount()

    def clean(self):
        """Deletes every child under this window"""
        for widge in self.widgets.values():
            widge.unmount()

    def mount(self):
        """Creates the window, children then calls the windows mainloop"""

        self.window = ct.CTk(**self._props.ctk)
        self.window.title(self.name)
        self.configure(**self._props.user)

        for widge in self.widgets.values():
            widge.setparent(self.window)
            widge.mount()

        self.window.mainloop()

    def unmount(self):
        """Deletes the window"""
        if self.window:
            self.window.destroy()

    def title(self, title: str):
        """Set the title of the window"""
        if title is not None:
            self.configure(title=title)

    def size(self, size: tuple = (75, 100)):
        """Set the size of the window"""
        self.configure(size=size)

    def position(self, pos: tuple = (133, 75)):
        """Set the position of the window"""
        self.configure(position=pos)

    def configure(self, *args, **kwargs):
        """Configure the window"""
        window = self.window is not None
        if "title" in kwargs:
            self._props.user["title"] = kwargs["title"]
            if window:
                self.window.title(kwargs.pop("title"))

        if "size" in kwargs:
            size = kwargs.pop("size")
            self._props.user["size"] = size
            if window:
                self.window.geometry(f"{size[0]}x{size[1]}")

        if "position" in kwargs:
            pos = kwargs.pop("position")
            size = self._props.user["size"]

            self._props.user["position"] = pos
            if window:
                self.window.geometry(f"{size[0]}x{size[1]}+{pos[0]}+{pos[1]}")

        if window:
            self.window.configure(*args, **kwargs)

    def __repr__(self) -> str:
        return f"Window(name={self.name}, widget_count={len(self.widgets)})"


if __name__ == "__main__":
    window = Window("Albekurki")
    window.configure(size=(75, 100), position=(133, 75))

    def cl():
        window.title(uuid.uuid4())

    window.addChild([
        Widget('CTkButton', properties=Widget.parse(
            relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4, text="AHHHHHHhhhh", command=cl))
    ])

    window.mount()
