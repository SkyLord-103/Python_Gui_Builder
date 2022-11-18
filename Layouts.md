# Layouts

## Layout another

```Python
class widget:
    name = "Frame.label.widget"
    widget = None # CTkObject
    ctkObject = None

    def __init__(ctkObject, properties):
        """Parses properties then makes the gui"""
        paresedProps = propParser(properties)
        self.ctkObject = ctkObject


    def place_configure(*args, **kwargs):
        widget.place_configure(*args, **kwargs)

    def removeChild(child: str):
        """Removes a child"""
    def addChild():
        """Adds a child to the widget"""
    def mount():
        """Creates every child under this widget"""
        self.widget = self.ctkObject(self.parsedProps.creation)
        self.widget.place_configure(self.parsedProps.place)

    def unmount():
        """Deletes anything child of this widget"""
        self.widget.destroy()

class Builder:
    def createWidget(widget: str, properties: dict, children: Optional[list[widget]]) -> widget:
        pass 


Builder.createWidget("Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5}, [
    Builder.createWidget("Frame", {"master": window, "relwidth": 0.5, "relheight": 0.5})
]).mount().unmount()
```

## Layout 1

```Python
Widget(
    Properties: dict,
    Place_Config: dict,
    children: Optional[List[Widget]]
).make() -> CTkObject
```

## Layout 2

```Python
Widget(master=None, text=None,
    placeholder_text=None, children: Optional[List[Widget]],
    **kw_plccfg
).make() -> CTkObject
```

## Layout 3

```Python
Widget(
    *arg_props, **kw_props
)(
    *arg_plccfg, **kw_plccfg
).make() -> CTkObject
```

## Layout 4?

```Python
widget = widget(*args, **kwargs)
widget.place_cfg(*args, **kwargs)
widget = widget.make()
```
