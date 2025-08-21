from customtkinter import CTk, CTkLabel

from services import home


class App(CTk):
    def __init__(self):
        super().__init__()

        self.configuration()
        self.interface()

    def configuration(self):
        # app size
        width_app = 350
        height_app = 400

        self.title("Customer Registration System")
        self.geometry(f"{width_app}x{height_app}")
        self.configure(fg_color="#3E3E3E")

    def interface(self):
        self.reg = home.HomeScreen(self)
        self.reg.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_version = CTkLabel(
            self,
            text="version: 0.0.1",
            text_color="#ffffff",
        )
        self.lbl_version.place(relx=0.74, rely=0.95, anchor="sw")
