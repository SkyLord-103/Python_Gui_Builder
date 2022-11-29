import widget_hiarchy as wid
import customtkinter as ctk


a = ctk.CTk()


l = wid.Label('CTkLabel', properties=wid.parse(
    master=a, relwidth=0.5, relheight=0.5, justify='s', fg_color="#aa97ff"),
    children=[])

l.mount()
a.mainloop()
