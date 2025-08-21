from customtkinter import CTk

from services import home, registration


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
        self.frames = {}  # dictionary to save the screens
        self.create_frames()
        self.show_frame("home")

    def create_frames(self):
        self.frames["home"] = home.HomeScreen(
            self,
            switch_screen=self.show_frame,
        )
        self.frames["registration"] = registration.Register(
            self,
            switch_screen=self.show_frame,
            on_cancel=lambda: self.show_frame("home"),  # return to home screen
        )

        for frame in self.frames.values():
            frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_frame(self, name):
        for key, frame in self.frames.items():
            frame.place_forget()
        self.frames[name].place(relx=0.5, rely=0.5, anchor="center")
