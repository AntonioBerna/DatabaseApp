from tkinter import *
import sqlite3

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App - Clever Code")
        self.root.geometry("400x600")

        # Use This Only One Times
        # self.__createDB()

        self.f_name = Entry(self.root, width=30)
        self.f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name = Entry(self.root, width=30)
        self.l_name.grid(row=1, column=1)
        self.address = Entry(self.root, width=30)
        self.address.grid(row=2, column=1)
        self.city = Entry(self.root, width=30)
        self.city.grid(row=3, column=1)
        self.state = Entry(self.root, width=30)
        self.state.grid(row=4, column=1)
        self.zipcode = Entry(self.root, width=30)
        self.zipcode.grid(row=5, column=1)
        self.delete_box = Entry(self.root, width=30)
        self.delete_box.grid(row=9, column=1, pady=5)

        self.f_name_label = Label(self.root, text="First Name:")
        self.f_name_label.grid(row=0, column=0, pady=(10, 0))
        self.l_name_label = Label(self.root, text="Last Name:")
        self.l_name_label.grid(row=1, column=0)
        self.address_label = Label(self.root, text="Address:")
        self.address_label.grid(row=2, column=0)
        self.city_label = Label(self.root, text="City:")
        self.city_label.grid(row=3, column=0)
        self.state_label = Label(self.root, text="State:")
        self.state_label.grid(row=4, column=0)
        self.zipcode_label = Label(self.root, text="Zipcode:")
        self.zipcode_label.grid(row=5, column=0)
        self.delete_box_label = Label(self.root, text="Select ID:")
        self.delete_box_label.grid(row=9, column=0, pady=5)

        self.submit_button = Button(self.root, text="Add Record To Database", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        self.query_button = Button(self.root, text="Show Records", command=self.query)
        self.query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=132)
        self.delete_button = Button(self.root, text="Delete Record", command=self.delete)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
        self.edit_button = Button(self.root, text="Edit Record", command=self.edit)
        self.edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    def __createDB(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
        )""")

        conn.commit()
        conn.close()

    def submit(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", {
            "f_name": self.f_name.get(),
            "l_name": self.l_name.get(),
            "address": self.address.get(),
            "city": self.city.get(),
            "state": self.state.get(),
            "zipcode": self.zipcode.get()
        })

        conn.commit()
        conn.close()

        self.f_name.delete(0, END)
        self.l_name.delete(0, END)
        self.address.delete(0, END)
        self.city.delete(0, END)
        self.state.delete(0, END)
        self.zipcode.delete(0, END)

    def query(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        # print(records)

        print_records = ""
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
        
        self.query_label = Label(self.root, text=print_records)
        self.query_label.grid(row=12, column=0, columnspan=2)

        conn.commit()
        conn.close()
    
    def delete(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid=" + self.delete_box.get())

        conn.commit()
        conn.close()

    def edit(self):
        self.editor = Tk()
        self.editor.title("Update A Record - Clever Code")

        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        record_id = self.delete_box.get()
        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
        records = c.fetchall()

        self.f_name_editor = Entry(self.editor, width=30)
        self.f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name_editor = Entry(self.editor, width=30)
        self.l_name_editor.grid(row=1, column=1)
        self.address_editor = Entry(self.editor, width=30)
        self.address_editor.grid(row=2, column=1)
        self.city_editor = Entry(self.editor, width=30)
        self.city_editor.grid(row=3, column=1)
        self.state_editor = Entry(self.editor, width=30)
        self.state_editor.grid(row=4, column=1)
        self.zipcode_editor = Entry(self.editor, width=30)
        self.zipcode_editor.grid(row=5, column=1)

        self.f_name_label = Label(self.editor, text="First Name:")
        self.f_name_label.grid(row=0, column=0, pady=(10, 0))
        self.l_name_label = Label(self.editor, text="Last Name:")
        self.l_name_label.grid(row=1, column=0)
        self.address_label = Label(self.editor, text="Address:")
        self.address_label.grid(row=2, column=0)
        self.city_label = Label(self.editor, text="City:")
        self.city_label.grid(row=3, column=0)
        self.state_label = Label(self.editor, text="State:")
        self.state_label.grid(row=4, column=0)
        self.zipcode_label = Label(self.editor, text="Zipcode:")
        self.zipcode_label.grid(row=5, column=0)

        for record in records:
            self.f_name_editor.insert(0, record[0])
            self.l_name_editor.insert(0, record[1])
            self.address_editor.insert(0, record[2])
            self.city_editor.insert(0, record[3])
            self.state_editor.insert(0, record[4])
            self.zipcode_editor.insert(0, record[5])

        conn.commit()
        conn.close()

        self.edit_button = Button(self.editor, text="Save Record", command=self.update)
        self.edit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    def update(self):
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        record_id = self.delete_box.get()
        c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid=:oid""", {
                "first": self.f_name_editor.get(),
                "last": self.l_name_editor.get(),
                "address": self.address_editor.get(),
                "city": self.city_editor.get(),
                "state": self.state_editor.get(),
                "zipcode": self.zipcode_editor.get(),
                "oid": record_id
            })

        conn.commit()
        conn.close()

        self.editor.destroy()

if __name__ == '__main__':
    root = Tk()
    DatabaseApp(root)
    root.mainloop()