import re  # For email validation
from tkinter import *
from tkinter import ttk  # For Treeview widget
from tkinter import messagebox  # For showing error messages

class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x500+180+120")  # Adjusted size to fit everything
        self.root.title("Customer Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # =================== Variables ===============
        self.cus_SearchBy = StringVar()
        self.cus_textSearch = StringVar()

        self.cus_id = StringVar()
        self.cus_name = StringVar()
        self.cus_email = StringVar()
        self.cus_contact = StringVar()
        self.cus_address = StringVar()
        self.cus_gender = StringVar()

        # ================== Search Frame =================
        SearchFrame = LabelFrame(self.root, text="Customer Search", font=("Arial", 12, 'bold'), bg="white", bd=2, relief=RIDGE)
        SearchFrame.place(x=50, y=20, width=900, height=70)

        cmd_search = ttk.Combobox(SearchFrame, textvariable=self.cus_SearchBy, values=('Select', 'Email', 'CustomerName', 'Contact', 'Address'), state="readonly", justify=CENTER, font=('Arial', 12))
        cmd_search.place(x=10, y=10, width=150)
        cmd_search.current(0)

        text_search = Entry(SearchFrame, textvariable=self.cus_textSearch, font=('Arial', 12), bg='lightgray')
        text_search.place(x=170, y=10, width=250)

        search_btn = Button(SearchFrame, text="Search", cursor='hand2', font=('Arial', 12, 'bold'), bg='green', fg='white')
        search_btn.place(x=440, y=8, width=120, height=30)

        # =============== Customer Details =================
        title = Label(self.root, text="Customer Details", font=('Arial', 15, 'bold'), bg='#0f4d7d', fg='white')
        title.place(x=0, y=100, relwidth=1, height=40)

        # =================== Form Fields ===================
        # Left Side (Labels and Entries)
        Label(self.root, text="Customer ID", font=('Arial', 12, 'bold'), bg="white").place(x=50, y=150)
        Entry(self.root, textvariable=self.cus_id, font=('Arial', 12), bg='lightyellow').place(x=200, y=150, width=200)

        Label(self.root, text="Name", font=('Arial', 12, 'bold'), bg="white").place(x=50, y=200)
        Entry(self.root, textvariable=self.cus_name, font=('Arial', 12), bg='white').place(x=200, y=200, width=200)

        Label(self.root, text="Gender", font=('Arial', 12, 'bold'), bg="white").place(x=50, y=250)
        gender_combo = ttk.Combobox(self.root, textvariable=self.cus_gender, values=('Select', 'Male', 'Female', 'Other'), state="readonly", justify=CENTER, font=('Arial', 12))
        gender_combo.place(x=200, y=250, width=200)
        gender_combo.current(0)

        # Right Side (Labels and Entries)
        Label(self.root, text="Contact", font=('Arial', 12, 'bold'), bg="white").place(x=500, y=150)
        Entry(self.root, textvariable=self.cus_contact, font=('Arial', 12), bg='lightgray').place(x=650, y=150, width=200)

        Label(self.root, text="Email", font=('Arial', 12, 'bold'), bg="white").place(x=500, y=200)
        Entry(self.root, textvariable=self.cus_email, font=('Arial', 12), bg='lightgray').place(x=650, y=200, width=200)

        Label(self.root, text="Address", font=('Arial', 12, 'bold'), bg="white").place(x=500, y=250)
        Entry(self.root, textvariable=self.cus_address, font=('Arial', 12), bg='white').place(x=650, y=250, width=200)

        # =================== Buttons ===================
        btn_frame = Frame(self.root, bg="white")
        btn_frame.place(x=50, y=300, width=900, height=40)

        btn_add = Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="#003366", fg="white", width=12)
        btn_add.grid(row=0, column=0, padx=10)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="#00796b", fg="white", width=12)
        btn_update.grid(row=0, column=1, padx=10)

        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#d84315", fg="white", width=12)
        btn_delete.grid(row=0, column=2, padx=10)

        # =================== Customer Table (Grid) ===================
        table_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        table_frame.place(x=50, y=350, width=900, height=200)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.customer_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Contact", "Email", "Gender", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("ID", text="Customer ID")
        self.customer_table.heading("Name", text="Name")
        self.customer_table.heading("Contact", text="Contact")
        self.customer_table.heading("Email", text="Email")
        self.customer_table.heading("Gender", text="Gender")
        self.customer_table.heading("Address", text="Address")

        self.customer_table["show"] = "headings"

        self.customer_table.column("ID", width=80)
        self.customer_table.column("Name", width=150)
        self.customer_table.column("Contact", width=120)
        self.customer_table.column("Email", width=180)
        self.customer_table.column("Gender", width=80)
        self.customer_table.column("Address", width=180)

        self.customer_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = customerClass(root)
    root.mainloop()