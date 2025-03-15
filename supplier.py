from tkinter import *
from tkinter import messagebox  # For showing error messages

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+0+0")  # Set initial size
        self.root.title("Supplier Management System")
        self.root.config(bg="lightblue")

        # Remove minimize, maximize, and close buttons
        self.root.overrideredirect(True)  # Removes window controls

        # Center the window on the screen
        self.center_window()

        # Add a custom close button
        btn_close = Button(self.root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white",
                           bd=0, command=self.root.destroy, cursor="hand2")
        btn_close.place(x=1060, y=10, width=30, height=30)

        # =================== SUPPLIER FORM ===================
        # Supplier Details Frame
        details_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        details_frame.place(x=50, y=50, width=1000, height=400)

        # Labels and Entries for Supplier Details
        labels = ["Supplier ID", "Supplier Name", "Contact", "Email", "Address"]
        self.entries = {}  # Dictionary to store entry widgets
        for i, text in enumerate(labels):
            lbl = Label(details_frame, text=text, font=("Arial", 12, "bold"), bg="white", fg="#333333")
            lbl.place(x=20, y=20 + i * 40)

            entry = Entry(details_frame, font=("Arial", 12), bd=2, relief=RIDGE)
            entry.place(x=200, y=20 + i * 40, width=300)
            self.entries[text] = entry  # Store entry widget

        # Buttons for Actions
        btn_add = Button(details_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                         bd=0, cursor="hand2", command=self.add_supplier)
        btn_add.place(x=200, y=250, width=100, height=30)

        btn_update = Button(details_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white",
                            bd=0, cursor="hand2", command=self.update_supplier)
        btn_update.place(x=350, y=250, width=100, height=30)

        btn_delete = Button(details_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            bd=0, cursor="hand2", command=self.delete_supplier)
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

    def validate_fields(self):
        """
        Validate if all required fields are filled.
        """
        for field, entry in self.entries.items():
            if not entry.get().strip():
                entry.focus_set()  # Focus on the empty field
                messagebox.showerror("Error", f"Please fill the {field} field!")
                return False
        return True

    def add_supplier(self):
        """
        Add a new supplier.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        supplier_id = self.entries["Supplier ID"].get()
        supplier_name = self.entries["Supplier Name"].get()
        contact = self.entries["Contact"].get()
        email = self.entries["Email"].get()
        address = self.entries["Address"].get()

        # Add to the database or table (you can replace this with your logic)
        messagebox.showinfo("Success", "Supplier added successfully!")
        # Clear entries after adding
        for entry in self.entries.values():
            entry.delete(0, END)

    def update_supplier(self):
        """
        Update selected supplier details.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        supplier_id = self.entries["Supplier ID"].get()
        supplier_name = self.entries["Supplier Name"].get()
        contact = self.entries["Contact"].get()
        email = self.entries["Email"].get()
        address = self.entries["Address"].get()

        # Update the supplier (you can replace this with your logic)
        messagebox.showinfo("Success", "Supplier updated successfully!")
        # Clear entries after updating
        for entry in self.entries.values():
            entry.delete(0, END)

    def delete_supplier(self):
        """
        Delete selected supplier.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        supplier_id = self.entries["Supplier ID"].get()

        # Delete the supplier (you can replace this with your logic)
        messagebox.showinfo("Success", "Supplier deleted successfully!")
        # Clear entries after deleting
        for entry in self.entries.values():
            entry.delete(0, END)


# Run the Application
if __name__ == "__main__":
    root = Tk()
    app = supplierClass(root)
    root.mainloop()