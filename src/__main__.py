import customtkinter as ctk


def main():
    window = ctk.CTk()

    frame = ctk.CTkFrame(master=window)
    frame.place_configure(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    def delete():
        frame.destroy()

    b = ctk.CTkButton(master=frame, text="World", command=delete)
    b.place_configure(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    window.mainloop()


if __name__ == "__main__":
    main()
