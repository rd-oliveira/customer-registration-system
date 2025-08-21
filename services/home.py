# Home screen of the customer registration system.

from customtkinter import CTkFrame, CTkButton, CTkImage
from PIL import Image


def load_image(path: str, image_size: tuple) -> CTkImage:
    return CTkImage(light_image=Image.open(path), size=image_size)


class MyButton(CTkButton):
    def __init__(
        self,
        master,
        image,
        width=64,
        heigth=64,
        text="",
        bg_color="transparent",
        fg_color="#4081EB",
        hover_color="#1C4B96",
    ):
        super().__init__(
            master,
            width=width,
            height=heigth,
            text=text,
            image=image,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
        )


class HomeScreen(CTkFrame):
    """
    HomeScreen class represents the main interface of the customer registration system,
    providing quick access to customer operations such as Create, Read, Update, and Delete (CRUD).
    """

    def __init__(self, master, width=200, height=200, fg_color="transparent"):
        super().__init__(master, width, height, fg_color=fg_color)

        # Buttons
        # register
        self.btn_register = MyButton(
            self, load_image("./assets/buttons/btn_create.png", (29, 30))
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
