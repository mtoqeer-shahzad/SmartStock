from tkinter import *
from PIL import Image, ImageTk  # For handling images
import time  # For updating the clock
from customer import customerClass  # Import customerClass from customer.py
from supplier import supplierClass  # Import supplierClass from supplier.py
from category import categoryClass  # Import categoryClass from category.py
from product import productClass  # Import productClass from product.py
from sale import saleClass  # Import saleClass from sale.py

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")  
        self.root.title("Inventory Management System")
        self.root.config(bg="#f8f8f8")  # Light gray background for the main window

        # =================== HEADER DESIGN ===================
        header = Canvas(self.root, height=80, bg="#003366", highlightthickness=0)
        header.pack(side="top", fill="x")
        header.create_rectangle(0, 0, 1220, 80, fill="#003366", outline="")

        # Load and Resize Image (Logo/Icon)
        try:
            img = Image.open("Images/inventory1.png")
            img = img.resize((60, 60), Image.LANCZOS)
            self.icon_title = ImageTk.PhotoImage(img)

            img_label = Label(self.root, image=self.icon_title, bg="#003366")
            img_label.place(x=20, y=10)
        except Exception as e:
            print("Error loading image:", e)

        # Header Title
        header_label = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM",
                             font=("Arial", 24, "bold"), fg="white", bg="#003366")
        header_label.place(x=100, y=20)

        # =================== CLOCK BELOW HEADER ===================
        self.clock_label = Label(self.root, font=("Arial", 14, "bold"), fg="white", bg="#005599")
        self.clock_label.pack(fill="x")  
        self.update_clock()  

        # =================== LOGOUT BUTTON ===================
        def on_enter(e):
            btn_logout.config(bg="#ff5050", fg="white")  # Coral red on hover

        def on_leave(e):
            btn_logout.config(bg="#003366", fg="white")  # Dark blue on leave

        btn_logout = Button(self.root, text='Logout', font=("Arial", 15, "bold"),
                            bg="#003366", fg="white", bd=0, relief=FLAT,
                            activebackground="#ff5050", activeforeground="white",
                            cursor="hand2")

        # Place the button at the top-right corner (Responsive)
        btn_logout.place(relx=1.0, x=-20, y=20, anchor="ne", width=120, height=40)

        btn_logout.bind("<Enter>", on_enter)
        btn_logout.bind("<Leave>", on_leave)

        # =================== LEFT SIDE BAR ===================
        self.leftBar = Frame(self.root, bd=2, relief=RIDGE, bg="#f8f8f8")  # Light gray background
        self.leftBar.place(x=0, y=108, width=200, height=500)

        # Load Sidebar Menu Image
        try:
            self.MenuLogo = Image.open("Images/inventory.png")  
            self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)  
            self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)  

            lbl_menuLogo = Label(self.leftBar, image=self.MenuLogo, bg="#f8f8f8")  
            lbl_menuLogo.pack(side=TOP, fill=X)  
        except Exception as e:
            print("Error loading menu image:", e)

        # =================== MENU BUTTONS (INDIVIDUAL) ===================
        Label(self.leftBar, text="Menu", font=("Arial", 14, "bold"), bg="#009688", fg="white").pack(pady=10)

        # Button Hover Effects
        def on_enter_button(e):
            e.widget.config(bg="#ff5050", fg="white")  # Coral red on hover

        def on_leave_button(e):
            e.widget.config(bg="#003366", fg="white")  # Dark blue on leave

        buttons = [
            ("Customer", self.customer_action),
            ("Supplier", self.supplier_action),
            ("Category", self.category_action),
            ("Products", self.products_action),
            ("Sale", self.sale_action),
            ("Exit", self.exit_action)
        ]

        for text, command in buttons:
            btn = Button(self.leftBar, text=text, font=("Arial", 15, "bold"),
                         bg="#003366", fg="white", bd=0, relief=FLAT,
                         activebackground="#ff5050", activeforeground="white",
                         cursor="hand2", command=command)
            btn.pack(fill="x", padx=10, pady=5)
            btn.bind("<Enter>", on_enter_button)
            btn.bind("<Leave>", on_leave_button)

        # =================== FOOTER ===================
        footer = Frame(self.root, bg="#003366", height=40)
        footer.pack(side=BOTTOM, fill=X)

        # Footer Text
        footer_label = Label(footer, text="Created by Coder", 
                             font=("Arial", 12, "bold"), fg="white", bg="#003366")
        footer_label.pack(pady=10)
        
        # =================== CONTENT ===================
        # Define categories and their positions
        categories = [
            {"text": "Employees\n[0]", "bg": "#005599", "x": 300, "y": 120},
            {"text": "Suppliers\n[0]", "bg": "#00796b", "x": 650, "y": 120},
            {"text": "Categories\n[0]", "bg": "#d84315", "x": 300, "y": 300},
            {"text": "Products\n[0]", "bg": "#6a1b9a", "x": 650, "y": 300},
        ]

        # Create and place labels for each category
        for category in categories:
            label = Label(self.root, text=category["text"], bg=category["bg"], 
                          font=("Arial", 14, "bold"), fg="white", bd=2, relief=RIDGE)
            label.place(x=category["x"], y=category["y"], height=150, width=300)

    # =================== CLOCK FUNCTION ===================
    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")  
        current_date = time.strftime("%A, %d %B %Y")  
        self.clock_label.config(text=f"{current_date}  |  Time: {current_time}")
        self.root.after(1000, self.update_clock)  

    # =================== BUTTON ACTIONS ===================
    def customer_action(self):
        print("Customer Button Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = customerClass(self.new_win)

    def supplier_action(self):
        print("Supplier Button Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category_action(self):
        print("Category Button Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def products_action(self):
        print("Products Button Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sale_action(self):
        print("Sale Button Clicked")
        self.new_win = Toplevel(self.root)
        self.new_obj = saleClass(self.new_win)

    def exit_action(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()