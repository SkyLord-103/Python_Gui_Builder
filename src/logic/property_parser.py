import customtkinter as ct
from argparse import Namespace

creation_keys = ["master", "text", "placeholder_text",
                 "command", "text_font", "width", "height"]
place_keys = ["relx", "rely", "relwidth", "relheight", "anchor", "x", "y"]

CTkObjects = {
    "CTkFrame": ct.CTkFrame,
    "CTkLabel": ct.CTkLabel,
    "CTkButton": ct.CTkButton,
    "CTkEntry": ct.CTkEntry,
    "CTkCheckBox": ct.CTkCheckBox,
}


def Parser(pureProps) -> Namespace:
    return Namespace(creation={k: v for k, v in pureProps.items() if k in creation_keys},
                     place={k: v for k, v in pureProps.items() if k in place_keys})


def ObjParser(obj: any) -> any:
    return CTkObjects.get(obj) if isinstance(obj, str) else obj
