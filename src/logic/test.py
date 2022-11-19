import customtkinter as ct
from widget import Widget
from rich.console import Console
console = Console()
w = ct.CTk()

button = None


def cl():
    print(cl.sframe)


subbtn = Widget(ct.CTkButton, name="sframe", master=w, text="CLICK", command=cl, relx=0.3,
                rely=0.3, relwidth=0.3, relheight=0.4)
console.print("FUCK:", subbtn.children)
button = Widget(ct.CTkButton, addedChildren=[
    subbtn
], master=w, text="string", relx=0.1,
    rely=0.1, relwidth=0.8, relheight=0.8, command=lambda: print("Hello")).mount()

# ,
# widget(ct.CTkButton, name="sbbutton", master=w, text="CLICK", command=cl, relx=0.45,
#    rely=0.3, relwidth=0.3, relheight=0.4)
w.mainloop()
