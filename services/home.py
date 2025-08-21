# Home screen of the customer registration system.

from customtkinter import CTkFrame, CTkButton, CTkImage, CTkLabel
from PIL import Image
from pathlib import Path


def load_image(path: str | Path, image_size: tuple) -> CTkImage:
    path = Path(path)
    return CTkImage(light_image=Image.open(path), size=image_size)


class MyButton(CTkButton):
    def __init__(
        self,
        master,
        image,
        width=64,
        height=64,
        text="",
        bg_color="transparent",
        fg_color="#4081EB",
        hover_color="#1C4B96",
        **kwargs,
    ):
        super().__init__(
            master,
            width=width,
            height=height,
            text=text,
            image=image,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            **kwargs,
        )


class HomeScreen(CTkFrame):
    """
    HomeScreen class represents the main interface of the customer registration system,
    providing quick access to customer operations such as Create, Read, Update, and Delete (CRUD).
    """

    def __init__(
        self, master, switch_screen, width=200, height=200, fg_color="transparent"
    ):
        super().__init__(master, width, height, fg_color=fg_color)

        self.switch_screen = switch_screen
        self.configuration()
        self.interface()

    def configuration(self):
        self.grid_rowconfigure(index=(0, 1), weight=1)
        self.grid_columnconfigure(index=(0, 1), weight=1)

    def interface(self):
        # Buttons
        # register
        self.btn_register = MyButton(
            self,
            load_image("./assets/buttons/btn_create.png", (29, 30)),
            command=lambda: self.switch_screen("registration"),
        )
        self.btn_register.grid(column=0, row=0, padx=10, pady=10)

        # reading
        self.btn_view_customers = MyButton(
            self, load_image("./assets/buttons/btn_read.png", (28, 30))
        )
        self.btn_view_customers.grid(column=1, row=0, padx=10, pady=10)

        # update
        self.btn_update_customers = MyButton(
            self, load_image("./assets/buttons/btn_update.png", (34, 30))
        )
        self.btn_update_customers.grid(column=0, row=1, padx=10, pady=10)

        # exclusion
        self.btn_delete_customer = MyButton(
            self, load_image("./assets/buttons/btn_delete.png", (28, 30))
        )
        self.btn_delete_customer.grid(column=1, row=1, padx=10, pady=10)

        self.lbl_version = CTkLabel(
            self,
            text="version: 0.0.1",
            text_color="#ffffff",
        )
        self.lbl_version.grid(column=1, row=2, sticky="e")
