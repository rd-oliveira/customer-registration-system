from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkImage
from PIL import Image


class Register(CTkFrame):
    def __init__(self, master, width=200, height=200, fg_color="transparent"):
        super().__init__(master, width=width, height=height, fg_color=fg_color)

        my_image = CTkImage(
            light_image=Image.open(r".\assets\customer_logo.png"),
            dark_image=Image.open(r".\assets\customer_logo.png"),
            size=((116, 125)),
        )

        self.customer_logo = CTkLabel(self, text="", image=my_image)
        self.customer_logo.pack(pady=5)

        self.txt_name = CTkEntry(self, placeholder_text="name")
        self.txt_name.pack(padx=5, pady=5, fill="x")

        self.birth = CTkEntry(self, placeholder_text="date of birth")
        self.birth.pack(padx=5, pady=5, fill="x")

        self.country = CTkEntry(self, placeholder_text="country")
        self.country.pack(padx=5, pady=5, fill="x")

        self.txt_mail = CTkEntry(self, placeholder_text="e-mail")
        self.txt_mail.pack(padx=5, pady=5, fill="x")

        self.frame_button = CTkFrame(self, fg_color="transparent")
        self.frame_button.pack(pady=10)

        self.btn_register = CTkButton(self.frame_button, text="Register")
        self.btn_register.pack(padx=5, side="left")

        self.btn_cancel = CTkButton(self.frame_button, text="Cancel")
        self.btn_cancel.pack(padx=5, side="right")
