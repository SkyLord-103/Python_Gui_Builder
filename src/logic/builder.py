from typing import Optional
from .widget import widget


class Builder:
    def createWidget(widget: str, properties: dict, children: Optional[list[widget]]) -> widget:
        pass
