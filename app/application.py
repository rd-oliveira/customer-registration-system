from customtkinter import CTk
from services import registration


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

    def interface(self):
        self.reg = registration.Register(self)
        self.reg.place(relx=0.5, rely=0.5, anchor='center')
