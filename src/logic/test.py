import customtkinter as ctk
from customtkinter import ThemeManager

from window import Window
from widget import Widget

window = Window()

_frame = Widget('CTkFrame', properties=Window.parse(
    master=window, anchor=ctk.CENTER, relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95))

# ========= Login text label =========#
create_label = Widget('CTkLabel', properties=Widget.parse(
    master=_frame, text="Create User", text_font=f"{ThemeManager.theme['text']['font']} 18 bold",
    anchor=ctk.N, relx=0.5, rely=0.01, relwidth=0.95, relheight=0.1
))
# create_label.element.text_label.place(
#     anchor=ctk.W, rely=0.5, x=0, y=0)

# ========= Labels =========#
username_label = Widget('CTkLabel', properties=Widget.parse(
    master=_frame, text="Username", text_font=f"{ThemeManager.theme['text']['font']} 10",
    anchor=ctk.N, relx=0.5, rely=0.4, relwidth=0.95, relheight=0.1))

window.addChild([create_label, username_label])
# username_label.element.text_label.place(
#     anchor=ctk.W, rely=0.5, x=0, y=0)

# self.password_label = CTkLabel(
#     master=self._frame, text="Password", text_font=f"{ThemeManager.theme['text']['font']} 10")
# self.password_label.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.325, relwidth=0.95, relheight=0.1)
# self.password_label.text_label.place(
#     anchor=tk.W, rely=0.5, x=0, y=0)

# self.confirm_label = CTkLabel(
#     master=self._frame, text="Confirm", text_font=f"{ThemeManager.theme['text']['font']} 10")
# self.confirm_label.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.53, relwidth=0.95, relheight=0.1)
# self.confirm_label.text_label.place(
#     anchor=tk.W, rely=0.5, x=0, y=0)

# self.login_label = CTkButton(
#     master=self._frame, text="Have an account?", text_font=f"{ThemeManager.theme['text']['font']} 10", text_color=ThemeManager.theme['color']['text'],
#     fg_color=ThemeManager.theme['color']['frame_low'], hover_color=ThemeManager.theme['color']['frame_low'], border_width=0)
# self.login_label.place_configure(
#     anchor=tk.N, relx=0.395, rely=0.89, relwidth=0.4, relheight=0.1)

# # ========= entries =========#
# self.username_entry = CTkEntry(master=self._frame,
#                                text_font=f"{ThemeManager.theme['text']['font']} 11")
# self.username_entry.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.22, relwidth=0.95, relheight=0.1)

# self.password_entry = CTkEntry(master=self._frame, show="●")
# self.password_entry.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.425, relwidth=0.95, relheight=0.1)

# self.confirm_entry = CTkEntry(master=self._frame, show="●")
# self.confirm_entry.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.63, relwidth=0.95, relheight=0.1)

# # ========= buttons yey =========#
# self.create_button = CTkButton(master=self._frame, text="Create",
#                                text_font=f"{ThemeManager.theme['text']['font']}", command=lambda: self.createEvent("hamburger"))
# self.create_button.place_configure(
#     anchor=tk.N, relx=0.5, rely=0.78, relwidth=0.95, relheight=0.1)

# self.login_button = CTkButton(
#     master=self._frame, text="Login", text_font=f"{ThemeManager.theme['text']['font']} 10", text_color=ThemeManager.theme['color']['button_link_blue'],
#     fg_color=ThemeManager.theme['color']['frame_low'], hover_color=ThemeManager.theme['color']['frame_low'], border_width=0, command=self.loginEvent)
# self.login_button.place_configure(
#     anchor=tk.N, relx=0.625, rely=0.89, relwidth=0.14, relheight=0.1)

window.mount()
