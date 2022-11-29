import customtkinter as _ctk
from argparse import Namespace as _nsp

_widget_creation_keys = [
    "master", "text", "placeholder_text", "command",
    "text_font", "text_color", "hover_color", "border_width",
    "width", "height", "fg_color", "afterCreate", "justify", "compound"
    "show"
]
_widget_place_keys = ["relx", "rely",
                      "relwidth", "relheight", "anchor", "x", "y"]

_window_ctk_keys = []
_window_user_keys = ["title", "size", "position", "anchor"]


_CTkObjects = {
    "CTkProgressBar": _ctk.CTkProgressBar,
    "CTkRadioButton": _ctk.CTkRadioButton,
    "CTkOptionMenu": _ctk.CTkOptionMenu,
    "CTkCheckBox": _ctk.CTkCheckBox,
    "CTkComboBox": _ctk.CTkComboBox,
    "CTkTextbox": _ctk.CTkTextbox,
    "CTkButton": _ctk.CTkButton,
    "CTkCanvas": _ctk.CTkCanvas,
    "CTkSlider": _ctk.CTkSlider,
    "CTkSwitch": _ctk.CTkSwitch,
    "CTkFrame": _ctk.CTkFrame,
    "CTkLabel": _ctk.CTkLabel,
    "CTkEntry": _ctk.CTkEntry
}


def _loop(d1, d2):
    return {k: v for k, v in d1.items() if k in d2}


def WindowParser(pureProps) -> _nsp:
    return _nsp(ctk=_loop(pureProps, _window_ctk_keys),
                user=_loop(pureProps, _window_user_keys))


def WidgetParser(pureProps) -> _nsp:
    return _nsp(ctk=_loop(pureProps, _widget_creation_keys),
                place=_loop(pureProps, _widget_place_keys))


def ObjParser(obj: any) -> any:
    return _CTkObjects.get(obj) if isinstance(obj, str) else obj
