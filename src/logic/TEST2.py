"""Just a test file :)

Creates a Create user window for the Password manager I'm making
"""

import customtkinter as ctk
from customtkinter import ThemeManager
import tkinter as tk

from window import Window
from widget import Widget

window = Window()


def setLeft(_, element):
    element.text_label.place(anchor=ctk.W, rely=0.5, x=0, y=0)


_frame = Widget('CTkFrame', properties=Widget.parse(
    anchor=ctk.CENTER, relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95),
    children=[
        Widget('CTkLabel', properties=Widget.parse(
            afterCreate=setLeft, text="Create User", text_font=f"{ThemeManager.theme['text']['font']} 18 bold",
            anchor=tk.N, relx=0.5, rely=0.01, relwidth=0.95, relheight=0.1)),
        Widget('CTkLabel', properties=Widget.parse(
            afterCreate=setLeft, text="Username", text_font=f"{ThemeManager.theme['text']['font']} 10",
            anchor=tk.N, relx=0.5, rely=0.12, relwidth=0.95, relheight=0.1)),
        Widget('CTkLabel', properties=Widget.parse(
            afterCreate=setLeft, text="Password", text_font=f"{ThemeManager.theme['text']['font']} 10",
            anchor=tk.N, relx=0.5, rely=0.325, relwidth=0.95, relheight=0.1)),
        Widget('CTkLabel', properties=Widget.parse(
            afterCreate=setLeft, text="Confirm", text_font=f"{ThemeManager.theme['text']['font']} 10",
            anchor=tk.N, relx=0.5, rely=0.53, relwidth=0.95, relheight=0.1)),
        Widget("CTkButton", properties=Widget.parse(
            text="Have an account?", text_font=f"{ThemeManager.theme['text']['font']} 10", text_color=ThemeManager.theme['color']['text'],
            fg_color=ThemeManager.theme['color']['frame_low'], hover_color=ThemeManager.theme['color']['frame_low'], border_width=0,
            anchor=tk.N, relx=0.395, rely=0.89, relwidth=0.4, relheight=0.1))
]
)


def recreate():
    # _frame.mount()
    window.clean()


# ========= entries =========#
username_entry = Widget("CTkEntry", properties=Widget.parse(
    text_font=f"{ThemeManager.theme['text']['font']} 11",
    anchor=tk.N, relx=0.5, rely=0.22, relwidth=0.95, relheight=0.1))


password_entry = Widget('CTkEntry', properties=Widget.parse(
    show="●", anchor=tk.N, relx=0.5, rely=0.425, relwidth=0.95, relheight=0.1))

confirm_entry = Widget('CTkEntry', properties=Widget.parse(
    show="●", anchor=tk.N, relx=0.5, rely=0.63, relwidth=0.95, relheight=0.1))

# # ========= buttons yey =========#
create_button = Widget('CTkButton', properties=Widget.parse(
    text="Create", text_font=f"{ThemeManager.theme['text']['font']}", command=lambda: print("Creating beyatch"),
    anchor=tk.N, relx=0.5, rely=0.78, relwidth=0.95, relheight=0.1))

login_button = Widget('CTkButton', properties=Widget.parse(
    text="Login", text_font=f"{ThemeManager.theme['text']['font']} 10", text_color="#00aa96", command=recreate,
    fg_color=ThemeManager.theme['color']['frame_low'], hover_color=ThemeManager.theme['color']['frame_low'], border_width=0,
    anchor=tk.N, relx=0.625, rely=0.89, relwidth=0.14, relheight=0.1))

_frame.addChild([
    username_entry, password_entry, confirm_entry, create_button, login_button
])
window.addChild(_frame)

window.mount()
