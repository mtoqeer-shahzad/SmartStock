from tkinter import *
from tkinter import ttk  # For Treeview widget
from tkinter import messagebox  # For showing error messages

class saleClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+0+0")  # Set initial size
        self.root.title("Sale Management System")
        self.root.config(bg="lightpink")

        # Remove minimize, maximize, and close buttons
        self.root.overrideredirect(True)  # Removes window controls

        # Center the window on the screen
        self.center_window()

        # Add a custom close button
        btn_close = Button(self.root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white",
                           bd=0, command=self.root.destroy, cursor="hand2")
        btn_close.place(x=1060, y=10, width=30, height=30)

        # =================== SALE FORM ===================
        # Sale Details Frame
        details_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        details_frame.place(x=50, y=50, width=1000, height=200)

        # Labels and Entries for Sale Details
        labels = ["Sale ID", "Product Name", "Quantity", "Price", "Total Amount"]
        self.entries = {}  # Dictionary to store entry widgets
        for i, text in enumerate(labels):
            lbl = Label(details_frame, text=text, font=("Arial", 12, "bold"), bg="white", fg="#333333")
            lbl.place(x=20, y=20 + i * 40)

            entry = Entry(details_frame, font=("Arial", 12), bd=2, relief=RIDGE)
            entry.place(x=200, y=10 + i * 40, width=300)
            self.entries[text] = entry  # Store entry widget

        # Buttons for Actions
        btn_add = Button(details_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                         bd=0, cursor="hand2", command=self.add_sale)
        btn_add.place(x=200, y=180, width=100, height=30)

        btn_update = Button(details_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white",
                            bd=0, cursor="hand2", command=self.update_sale)
        btn_update.place(x=350, y=180, width=100, height=30)

        btn_delete = Button(details_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            bd=0, cursor="hand2", command=self.delete_sale)
        btn_delete.place(x=500, y=180, width=100, height=30)

        # =================== SEARCH BAR ===================
        # Search Bar Frame
        search_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        search_frame.place(x=50, y=260, width=1000, height=50)

        # Search Label
        lbl_search = Label(search_frame, text="Search By:", font=("Arial", 12, "bold"), bg="white", fg="#333333")
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Search Entry
        self.search_entry = Entry(search_frame, font=("Arial", 12), bd=2, relief=RIDGE, width=40)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Search Button
        btn_search = Button(search_frame, text="Search", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                             width=12, command=self.search_data)
        btn_search.grid(row=0, column=2, padx=10, pady=10)

        # Clear Search Button
        btn_clear = Button(search_frame, text="Clear", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            width=12, command=self.clear_search)
        btn_clear.grid(row=0, column=3, padx=10, pady=10)

        # =================== GRID (TABLE) TO SHOW DATA ===================
        # Treeview Widget for Grid
        self.sale_table = ttk.Treeview(self.root, columns=("Sale ID", "Product Name", "Quantity", "Price", "Total Amount"), show="headings")
        self.sale_table.place(x=50, y=320, width=1000, height=150)  # Adjusted height and width

        # Add Scrollbars
        scroll_y = Scrollbar(self.root, orient=VERTICAL, command=self.sale_table.yview)
        scroll_y.place(x=1050, y=320, height=150)
        self.sale_table.configure(yscrollcommand=scroll_y.set)

        scroll_x = Scrollbar(self.root, orient=HORIZONTAL, command=self.sale_table.xview)
        scroll_x.place(x=50, y=470, width=1000)
        self.sale_table.configure(xscrollcommand=scroll_x.set)

        # Define Column Headings
        self.sale_table.heading("Sale ID", text="Sale ID")
        self.sale_table.heading("Product Name", text="Product Name")
        self.sale_table.heading("Quantity", text="Quantity")
        self.sale_table.heading("Price", text="Price")
        self.sale_table.heading("Total Amount", text="Total Amount")

        # Define Column Widths
        self.sale_table.column("Sale ID", width=100, anchor=CENTER)
        self.sale_table.column("Product Name", width=200, anchor=CENTER)
        self.sale_table.column("Quantity", width=100, anchor=CENTER)
        self.sale_table.column("Price", width=100, anchor=CENTER)
        self.sale_table.column("Total Amount", width=150, anchor=CENTER)

        # Add Sample Data to the Grid
        self.add_sample_data()

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

    def add_sample_data(self):
        """
        Add sample data to the grid (table).
        """
        sample_data = [
            ("S001", "Laptop", "5", "50000", "250000"),
            ("S002", "Mobile", "10", "20000", "200000"),
            ("S003", "Tablet", "8", "15000", "120000"),
            ("S004", "Printer", "3", "10000", "30000"),
        ]

        for data in sample_data:
            self.sale_table.insert("", "end", values=data)

    def search_data(self):
        """
        Search data in the Treeview based on the search term.
        """
        search_term = self.search_entry.get().strip().lower()  # Get the search term and convert to lowercase

        # Clear previous search results
        for row in self.sale_table.get_children():
            self.sale_table.delete(row)

        # Add rows that match the search term
        sample_data = [
            ("S001", "Laptop", "5", "50000", "250000"),
            ("S002", "Mobile", "10", "20000", "200000"),
            ("S003", "Tablet", "8", "15000", "120000"),
            ("S004", "Printer", "3", "10000", "30000"),
        ]

        for data in sample_data:
            if search_term in " ".join(data).lower():  # Check if search term exists in any field
                self.sale_table.insert("", "end", values=data)

    def clear_search(self):
        """
        Clear the search and display all data.
        """
        self.search_entry.delete(0, END)  # Clear the search entry
        for row in self.sale_table.get_children():
            self.sale_table.delete(row)  # Clear the Treeview
        self.add_sample_data()  # Re-add all sample data

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

    def add_sale(self):
        """
        Add a new sale.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        sale_id = self.entries["Sale ID"].get()
        product_name = self.entries["Product Name"].get()
        quantity = self.entries["Quantity"].get()
        price = self.entries["Price"].get()
        total_amount = self.entries["Total Amount"].get()

        # Add to the table
        self.sale_table.insert("", "end", values=(sale_id, product_name, quantity, price, total_amount))
        # Clear entries after adding
        for entry in self.entries.values():
            entry.delete(0, END)

    def update_sale(self):
        """
        Update selected sale details.
        """
        selected_item = self.sale_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a sale to update!")
            return  # Stop if no sale is selected

        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        sale_id = self.entries["Sale ID"].get()
        product_name = self.entries["Product Name"].get()
        quantity = self.entries["Quantity"].get()
        price = self.entries["Price"].get()
        total_amount = self.entries["Total Amount"].get()

        # Update the selected row
        self.sale_table.item(selected_item, values=(sale_id, product_name, quantity, price, total_amount))
        # Clear entries after updating
        for entry in self.entries.values():
            entry.delete(0, END)

    def delete_sale(self):
        """
        Delete selected sale from the table.
        """
        selected_item = self.sale_table.selection()
        if selected_item:
            self.sale_table.delete(selected_item)


# Run the Application
if __name__ == "__main__":
    root = Tk()
    app = saleClass(root)
    root.mainloop()