import re  # For email validation
from tkinter import *
from tkinter import ttk  # For Treeview widget
from tkinter import messagebox  # For showing error messages

class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x750+0+0")  # Adjusted size to fit everything
        self.root.title("Customer Management System.")
        self.root.config(bg="orange")

        # Remove minimize, maximize, and close buttons
        self.root.overrideredirect(True)  # Removes window controls

        # Center the window on the screen
        self.center_window()

        # Add a custom close button
        btn_close = Button(self.root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white",
                           command=self.root.destroy)
        btn_close.place(x=1160, y=10, width=30, height=30)  # Adjusted position for 1200x750 window

        # =================== CUSTOMER DASHBOARD ===================
        # Dashboard Frame
        dashboard_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        dashboard_frame.place(x=50, y=50, width=1100, height=650)

        # Dashboard Title
        lbl_title = Label(dashboard_frame, text="Customer Details", font=("Arial", 20, "bold"), bg="white", fg="#003366")
        lbl_title.pack(side=TOP, fill=X, pady=10)

        # =================== CUSTOMER DETAILS FORM ===================
        # Customer Details Frame
        details_frame = Frame(dashboard_frame, bg="white", bd=2, relief=RIDGE)
        details_frame.place(x=20, y=50, width=1060, height=250)  # Increased height for proper spacing

        # Buttons Frame (placed on the left side of the form)
        btn_frame = Frame(details_frame, bg="white")
        btn_frame.place(x=10, y=10, width=120, height=200)  # Adjusted position and size

        # Add Buttons
        btn_add = Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white",
                         width=10, command=self.add_customer)
        btn_add.pack(pady=10)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white",
                            width=10, command=self.update_customer)
        btn_update.pack(pady=10)

        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white",
                            width=10, command=self.delete_customer)
        btn_delete.pack(pady=10)

        # Labels and Entries for Customer Details
        labels = ["Customer ID", "Name", "Contact", "Email", "Address"]
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
        self.customer_table = ttk.Treeview(dashboard_frame, columns=("Customer ID", "Name", "Contact", "Email", "Address"), show="headings")
        self.customer_table.place(x=20, y=370, width=1060, height=250)  # Adjusted height and width

        # Add Scrollbars
        scroll_y = Scrollbar(dashboard_frame, orient=VERTICAL, command=self.customer_table.yview)
        scroll_y.place(x=1080, y=370, height=250)
        self.customer_table.configure(yscrollcommand=scroll_y.set)

        scroll_x = Scrollbar(dashboard_frame, orient=HORIZONTAL, command=self.customer_table.xview)
        scroll_x.place(x=20, y=620, width=1060)
        self.customer_table.configure(xscrollcommand=scroll_x.set)

        # Define Column Headings
        self.customer_table.heading("Customer ID", text="Customer ID")
        self.customer_table.heading("Name", text="Name")
        self.customer_table.heading("Contact", text="Contact")
        self.customer_table.heading("Email", text="Email")
        self.customer_table.heading("Address", text="Address")

        # Define Column Widths
        self.customer_table.column("Customer ID", width=100, anchor=CENTER)
        self.customer_table.column("Name", width=200, anchor=CENTER)
        self.customer_table.column("Contact", width=150, anchor=CENTER)
        self.customer_table.column("Email", width=250, anchor=CENTER)
        self.customer_table.column("Address", width=250, anchor=CENTER)

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
            ("C001", "John Doe", "1234567890", "john@example.com", "123 Main St"),
            ("C002", "Jane Smith", "0987654321", "jane@example.com", "456 Elm St"),
            ("C003", "Alice Johnson", "1122334455", "alice@example.com", "789 Oak St"),
            ("C004", "Bob Brown", "2233445566", "bob@example.com", "321 Pine St"),
            ("C005", "Charlie Davis", "3344556677", "charlie@example.com", "654 Birch St"),
            ("C006", "Diana Evans", "4455667788", "diana@example.com", "987 Cedar St"),
        ]

        for data in sample_data:
            self.customer_table.insert("", "end", values=data)

    def search_data(self):
        """
        Search data in the Treeview based on the search term.
        """
        search_term = self.search_entry.get().strip().lower()  # Get the search term and convert to lowercase

        # Clear previous search results
        for row in self.customer_table.get_children():
            self.customer_table.delete(row)

        # Add rows that match the search term
        sample_data = [
            ("C001", "John Doe", "1234567890", "john@example.com", "123 Main St"),
            ("C002", "Jane Smith", "0987654321", "jane@example.com", "456 Elm St"),
            ("C003", "Alice Johnson", "1122334455", "alice@example.com", "789 Oak St"),
            ("C004", "Bob Brown", "2233445566", "bob@example.com", "321 Pine St"),
            ("C005", "Charlie Davis", "3344556677", "charlie@example.com", "654 Birch St"),
            ("C006", "Diana Evans", "4455667788", "diana@example.com", "987 Cedar St"),
        ]

        for data in sample_data:
            if search_term in " ".join(data).lower():  # Check if search term exists in any field
                self.customer_table.insert("", "end", values=data)

    def clear_search(self):
        """
        Clear the search and display all data.
        """
        self.search_entry.delete(0, END)  # Clear the search entry
        for row in self.customer_table.get_children():
            self.customer_table.delete(row)  # Clear the Treeview
        self.add_sample_data()  # Re-add all sample data

    def validate_email(self, email):
        """
        Validate the email format using regex.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

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

    def add_customer(self):
        """
        Add a new customer to the table.
        """
        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Validate email
        email = self.entries["Email"].get().strip()
        if not self.validate_email(email):
            self.entries["Email"].focus_set()  # Focus on the email field
            messagebox.showerror("Error", "Invalid email format! Please enter a valid email.")
            return  # Stop if email is invalid

        # Get data from entries
        customer_id = self.entries["Customer ID"].get()
        name = self.entries["Name"].get()
        contact = self.entries["Contact"].get()
        address = self.entries["Address"].get()

        # Add to the table
        self.customer_table.insert("", "end", values=(customer_id, name, contact, email, address))
        # Clear entries after adding
        for entry in self.entries.values():
            entry.delete(0, END)

    def update_customer(self):
        """
        Update selected customer details.
        """
        selected_item = self.customer_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a customer to update!")
            return  # Stop if no customer is selected

        # Validate fields
        if not self.validate_fields():
            return  # Stop if validation fails

        # Validate email
        email = self.entries["Email"].get().strip()
        if not self.validate_email(email):
            self.entries["Email"].focus_set()  # Focus on the email field
            messagebox.showerror("Error", "Invalid email format! Please enter a valid email.")
            return  # Stop if email is invalid

        # Get data from entries
        customer_id = self.entries["Customer ID"].get()
        name = self.entries["Name"].get()
        contact = self.entries["Contact"].get()
        address = self.entries["Address"].get()

        # Update the selected row
        self.customer_table.item(selected_item, values=(customer_id, name, contact, email, address))
        # Clear entries after updating
        for entry in self.entries.values():
            entry.delete(0, END)

    def delete_customer(self):
        """
        Delete selected customer from the table.
        """
        selected_item = self.customer_table.selection()
        if selected_item:
            self.customer_table.delete(selected_item)


# Run the Application
if __name__ == "__main__":
    root = Tk()
    app = customerClass(root)
    root.mainloop()