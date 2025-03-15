import re  # For validation
from tkinter import *
from tkinter import ttk  # For Treeview widget
from tkinter import messagebox  # For showing error messages

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x750+0+0")  # Adjusted size to fit everything
        self.root.title("Category Management System")
        self.root.config(bg="orange")

        # Remove minimize, maximize, and close buttons
        self.root.overrideredirect(True)  # Removes window controls

        # Center the window on the screen
        self.center_window()

        # Add a custom close button
        btn_close = Button(self.root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white",
                           command=self.root.destroy)
        btn_close.place(x=1160, y=10, width=30, height=30)  # Adjusted position for 1200x750 window

        # =================== CATEGORY DASHBOARD ===================
        # Dashboard Frame
        dashboard_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        dashboard_frame.place(x=50, y=50, width=1100, height=650)

        # Dashboard Title
        lbl_title = Label(dashboard_frame, text="Category Dashboard", font=("Arial", 20, "bold"), bg="white", fg="#003366")
        lbl_title.pack(side=TOP, fill=X, pady=10)

        # =================== CATEGORY DETAILS FORM ===================
        # Category Details Frame
        details_frame = Frame(dashboard_frame, bg="white", bd=2, relief=RIDGE)
        details_frame.place(x=20, y=50, width=1060, height=250)  # Increased height for proper spacing

        # Buttons Frame (placed on the left side of the form)
        btn_frame = Frame(details_frame, bg="white")
        btn_frame.place(x=10, y=10, width=120, height=200)  # Adjusted position and size

        # Add Buttons
        btn_add = Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                         width=10, command=self.add_category)
        btn_add.pack(pady=10)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white",
                            width=10, command=self.update_category)
        btn_update.pack(pady=10)

        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            width=10, command=self.delete_category)
        btn_delete.pack(pady=10)

        # Labels and Entries for Category Details
        labels = ["Category ID", "Category Name", "Description"]
        self.entries = {}  # Dictionary to store entry widgets
        for i, text in enumerate(labels):
            lbl = Label(details_frame, text=text, font=("Arial", 12, "bold"), bg="white", fg="#333333")
            lbl.place(x=150, y=20 + i * 40)  # Adjusted position

            entry = Entry(details_frame, font=("Arial", 12), bd=2, relief=RIDGE, width=40)
            entry.place(x=300, y=20 + i * 40)  # Adjusted position
            self.entries[text] = entry  # Store entry widget

        # =================== SEARCH BAR ===================
        # Search Bar Frame
        search_frame = Frame(dashboard_frame, bg="white", bd=2, relief=RIDGE)
        search_frame.place(x=20, y=310, width=1060, height=50)

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
        self.category_table = ttk.Treeview(dashboard_frame, columns=("Category ID", "Category Name", "Description"), show="headings")
        self.category_table.place(x=20, y=370, width=1060, height=250)  # Adjusted height and width

        # Add Scrollbars
        scroll_y = Scrollbar(dashboard_frame, orient=VERTICAL, command=self.category_table.yview)
        scroll_y.place(x=1080, y=370, height=250)
        self.category_table.configure(yscrollcommand=scroll_y.set)

        scroll_x = Scrollbar(dashboard_frame, orient=HORIZONTAL, command=self.category_table.xview)
        scroll_x.place(x=20, y=620, width=1060)
        self.category_table.configure(xscrollcommand=scroll_x.set)

        # Define Column Headings
        self.category_table.heading("Category ID", text="Category ID")
        self.category_table.heading("Category Name", text="Category Name")
        self.category_table.heading("Description", text="Description")

        # Define Column Widths
        self.category_table.column("Category ID", width=100, anchor=CENTER)
        self.category_table.column("Category Name", width=200, anchor=CENTER)
        self.category_table.column("Description", width=500, anchor=CENTER)

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
        x = (screen_width - 1200) // 2  # 1200 is the window width
        y = (screen_height - 750) // 2  # 750 is the window height

        # Set the window position
        self.root.geometry(f"1200x750+{x}+{y}")

    def add_sample_data(self):
        """
        Add sample data to the grid (table).
        """
        sample_data = [
            ("CAT001", "Electronics", "Devices and gadgets"),
            ("CAT002", "Clothing", "Apparel and accessories"),
            ("CAT003", "Furniture", "Home and office furniture"),
            ("CAT004", "Books", "Educational and recreational books"),
        ]

        for data in sample_data:
            self.category_table.insert("", "end", values=data)

    def search_data(self):
        """
        Search data in the Treeview based on the search term.
        """
        search_term = self.search_entry.get().strip().lower()  # Get the search term and convert to lowercase

        # Clear previous search results
        for row in self.category_table.get_children():
            self.category_table.delete(row)

        # Add rows that match the search term
        sample_data = [
            ("CAT001", "Electronics", "Devices and gadgets"),
            ("CAT002", "Clothing", "Apparel and accessories"),
            ("CAT003", "Furniture", "Home and office furniture"),
            ("CAT004", "Books", "Educational and recreational books"),
        ]

        for data in sample_data:
            if search_term in " ".join(data).lower():  # Check if search term exists in any field
                self.category_table.insert("", "end", values=data)

    def clear_search(self):
        """
        Clear the search and display all data.
        """
        self.search_entry.delete(0, END)  # Clear the search entry
        for row in self.category_table.get_children():
            self.category_table.delete(row)  # Clear the Treeview
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

    def add_category(self):
        """
        Add a new category to the table.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        category_id = self.entries["Category ID"].get()
        category_name = self.entries["Category Name"].get()
        description = self.entries["Description"].get()

        # Add to the table
        self.category_table.insert("", "end", values=(category_id, category_name, description))
        # Clear entries after adding
        for entry in self.entries.values():
            entry.delete(0, END)

    def update_category(self):
        """
        Update selected category details.
        """
        selected_item = self.category_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a category to update!")
            return  # Stop if no category is selected

        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Get data from entries
        category_id = self.entries["Category ID"].get()
        category_name = self.entries["Category Name"].get()
        description = self.entries["Description"].get()

        # Update the selected row
        self.category_table.item(selected_item, values=(category_id, category_name, description))
        # Clear entries after updating
        for entry in self.entries.values():
            entry.delete(0, END)

    def delete_category(self):
        """
        Delete selected category from the table.
        """
        selected_item = self.category_table.selection()
        if selected_item:
            self.category_table.delete(selected_item)


# Run the Application
if __name__ == "__main__":
    root = Tk()
    app = categoryClass(root)
    root.mainloop()