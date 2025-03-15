from tkinter import *

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+0+0")  # Set initial size
        self.root.title("Product Management System")
        self.root.config(bg="lightyellow")

        # Remove minimize, maximize, and close buttons
        self.root.overrideredirect(True)  # Removes window controls

        # Center the window on the screen
        self.center_window()

        # Add a custom close button
        btn_close = Button(self.root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white",
                           bd=0, command=self.root.destroy, cursor="hand2")
        btn_close.place(x=1060, y=10, width=30, height=30)

        # =================== PRODUCT FORM ===================
        # Product Details Frame
        details_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        details_frame.place(x=50, y=50, width=1000, height=400)

        # Labels and Entries for Product Details
        labels = ["Product ID", "Product Name", "Category", "Price", "Quantity"]
        for i, text in enumerate(labels):
            lbl = Label(details_frame, text=text, font=("Arial", 12, "bold"), bg="white", fg="#333333")
            lbl.place(x=20, y=20 + i * 40)

            entry = Entry(details_frame, font=("Arial", 12), bd=2, relief=RIDGE)
            entry.place(x=200, y=20 + i * 40, width=300)

        # Buttons for Actions
        btn_add = Button(details_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                         bd=0, cursor="hand2")
        btn_add.place(x=200, y=250, width=100, height=30)

        btn_update = Button(details_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white",
                            bd=0, cursor="hand2")
        btn_update.place(x=350, y=250, width=100, height=30)

        btn_delete = Button(details_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            bd=0, cursor="hand2")
        btn_delete.place(x=500, y=250, width=100, height=30)

    def center_window(self):
        """
        Center the window on the screen.
        """
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width - 1100) // 2  # 1100 is the window width
        y = (screen_height - 500) // 2  # 500 is the window height

        # Set the window position
        self.root.geometry(f"1100x500+{x}+{y}")