import customtkinter as ctk
from argparse import Namespace

widget_creation_keys = [
    "master", "text", "placeholder_text", "command",
    "text_font", "text_color", "hover_color", "border_width",
    "width", "height", "fg_color", "afterCreate", "justify", "compound"
    "show"
]
widget_place_keys = ["relx", "rely",
                     "relwidth", "relheight", "anchor", "x", "y"]

window_ctk_keys = []
window_user_keys = ["title", "size", "position", "anchor"]


CTkObjects = {
    "CTkProgressBar": ctk.CTkProgressBar,
    "CTkRadioButton": ctk.CTkRadioButton,
    "CTkOptionMenu": ctk.CTkOptionMenu,
    "CTkCheckBox": ctk.CTkCheckBox,
    "CTkComboBox": ctk.CTkComboBox,
    "CTkTextbox": ctk.CTkTextbox,
    "CTkButton": ctk.CTkButton,
    "CTkCanvas": ctk.CTkCanvas,
    "CTkSlider": ctk.CTkSlider,
    "CTkSwitch": ctk.CTkSwitch,
    "CTkFrame": ctk.CTkFrame,
    "CTkLabel": ctk.CTkLabel,
    "CTkEntry": ctk.CTkEntry
}


def _loop(d1, d2):
    return {k: v for k, v in d1.items() if k in d2}


def WindowParser(pureProps) -> Namespace:
    return Namespace(ctk=_loop(pureProps, window_ctk_keys),
                     user=_loop(pureProps, window_user_keys))


def WidgetParser(pureProps) -> Namespace:
    return Namespace(creation=_loop(pureProps, widget_creation_keys),
                     place=_loop(pureProps, widget_place_keys))


def ObjParser(obj: any) -> any:
    return CTkObjects.get(obj) if isinstance(obj, str) else obj
