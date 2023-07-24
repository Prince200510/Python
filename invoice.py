#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      prince
#
# Created:     20-07-2023
# Copyright:   (c) prince 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Pmw
import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from datetime import date


def login():
    if username_entry.get() == 'prince':
        if password_entry.get() == '1001':
            login_window.withdraw()
            window.deiconify()
        else:
            messagebox.showerror("Login Error", "Invalid password. Please try again.")
    elif username_entry.get() == 'admin':
        if password_entry.get() == '1002':
            login_window.withdraw()
            window.deiconify()
        else:
            messagebox.showerror("Login Error", "Invalid password. Please try again.")
    else:
        messagebox.showerror("Login Error", "Invalid username. Please try again.")

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x400+600+100")
login_window.config(bg="#FEF9E7")
login_window.resizable(False, False)

login_label = tk.Label(login_window, text="Please log in to continue:", font=('times new roman', 14, 'bold'), bg="#FEF9E7")
login_label.pack(pady=10)

username_label = tk.Label(login_window, text='Username:', font=('times new roman', 12, 'bold'), bg="#FEF9E7")
username_label.pack(pady=5)
username_entry = tk.Entry(login_window, font=('arial', 12), width=20, bd=5, relief=tk.RIDGE)
username_entry.pack(pady=5)

password_label = tk.Label(login_window, text='Password:', font=('times new roman', 12, 'bold'), bg="#FEF9E7")
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, show='*', font=('arial', 12), width=20, bd=5, relief=tk.RIDGE)
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=login, font=('arial', 12, 'bold'), bg='#27AE60', fg='white', relief=tk.RIDGE)
login_button.pack(pady=10)

window = tk.Tk()
window.withdraw()
window.title("Invoice")
window.geometry("1350x900+600+100")
window.config(bg="#FEF9E7")
window.resizable(False, False)

head = tk.Label(window, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='black', fg='white', bd=14, relief=tk.RIDGE)
head.pack(fill=tk.X)
customer_frame = tk.LabelFrame(window, text=' Customer Detail ', font=('times new roman', 12, 'bold'), bg='black', fg='white', bd=8, relief=tk.RIDGE)
customer_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)
name_label = tk.Label(customer_frame, text='Name:', font=('times new roman', 12, 'bold'), bg='black', fg='white')
name_label.grid(row=0, column=0, padx=20)
name_entry = tk.Entry(customer_frame, font=('arial', 12), width=18, bd=5, relief=tk.RIDGE)
name_entry.grid(row=0, column=1)
phone_label = tk.Label(customer_frame, text='Phone Number:', font=('times new roman', 12, 'bold'), bg='black', fg='white')
phone_label.grid(row=0, column=3, padx=20)
phone_entry = tk.Entry(customer_frame, font=('arial', 12), width=18, bd=5, relief=tk.RIDGE)
phone_entry.grid(row=0, column=4)
bill_no_label = tk.Label(customer_frame, text='Bill No.:', font=('times new roman', 12, 'bold'), bg='black', fg='white')
bill_no_label.grid(row=0, column=5, padx=20)
billno_entry = tk.Entry(customer_frame, font=('arial', 12), width=12, bd=5, relief=tk.RIDGE)
billno_entry.grid(row=0, column=6)
billno_entry.insert(0, "1")


item_frame = tk.LabelFrame(window, text=' Item detail ', font=('times new roman', 12, 'bold'), bg='black', fg='white', bd=8, relief=tk.RIDGE)
item_frame.pack(side = 'left', padx=10, pady=10, ipadx=10, ipady=145, anchor="nw")
def combobox(event):
    global selected_item
    selected_item = item_combobox.get()
item_prices = {
    "Digestive Biscuits Price    ",
    "Cream Biscuits         ",
    "Marie Biscuits         ",
    "Bourbon Biscuits       ",
    "Oreo Biscuits          ",
    "Chocolate Chip Biscuits",
    "Ginger Biscuits        ",
    "Shortbread Biscuits    ",
    "Butter Biscuits        ",
    "Coconut Biscuits       ",
}
biscuit_label = tk.Label(item_frame, text='Biscuits :', font=('times new roman', 12, 'bold'), bg='black', fg='white')
biscuit_label.grid(row=0, column=0)


grocery_items = [
"Digestive Biscuits      Price -  50",
"Cream Biscuits          Price -  25",
"Marie Biscuits Large    Price -  70",
"Marie Biscuits Medium   Price -  30",
"Marie Biscuits Small    Price -  10",
"Bourbon Biscuits        Price -  50",
"Oreo Biscuits           Price -  35",
"Chocolate Chip Biscuits Price -  70",
"Ginger Biscuits         Price -  20",
"Shortbread Biscuits     Price -  90",
"Butter Biscuits         Price -  10",
"Coconut Biscuits        Price -  20"]

def combobox1(event):
    global selected_item
    selected_item = item_combobox1.get()

item_prices = {
    "Balaji Chip Tomato",
    "Lay's Classic",
    "Spice Wafer",
    "Pringles Sour Cream & Onion",
    "Uncle Chipps",
    "Haldiram's Aloo Bhujia",
    "Kurkure Masala Munch",
    "Bingo! Mad Angles",
    "Bikano Aloo Bhujia",
    "Cornitos Nacho Crisps",
    "Wafer Biscuits"
}

grocery_items1 = [
"Balaji Chip Tomato      Price -  50",
"Lay's Classic           Price -  50",
"Spice Wafer             Price -  50",
"Pringles Sour Cream     Price -  50",
"Uncle Chipps            Price -  50",
"Haldiram's Aloo Bhujia  Price -  50",
"Kurkure Masala Munch    Price -  50",
"Bingo! Mad Angles       Price -  50",
"Bikano Aloo Bhujia      Price -  50",
"Cornitos Nacho Crisps   Price -  50",]

item_combobox = ttk.Combobox(item_frame, values=grocery_items, state='readonly', width=30)
item_combobox.grid(row=1, column=0, padx=10, pady=15)
item_combobox.bind('<<ComboboxSelected>>', combobox)

item_combobox1 = ttk.Combobox(item_frame, values=grocery_items1, state='readonly', width=30)
item_combobox1.grid(row=4, column=0, padx=10, pady=15)
item_combobox1.bind('<<ComboboxSelected>>', combobox1)

def add():
    global selected_item
    if selected_item:

        quantity = qtn_combobox.get()  # Get the selected quantity
        multiline_text.insert(tk.END, f"{selected_item} - Quantity: {quantity}\n")
        selected_item = ""

selected_item = ""

def clear_item():
    selected_item = multiline_text.get("end-2c linestart", "end-1c lineend")
    if selected_item:
        multiline_text.delete("end-2c linestart", "end-1c lineend")

selected_item = ""
wafer_label = tk.Label(item_frame, text='Wafers or chips :', font=('times new roman', 12, 'bold'), bg='black', fg='white')
wafer_label.grid(row=3, column=0)






biscuit_button = tk.Button(item_frame, text='Add', command=add, font=('arial', 12, 'bold'), bg='#27AE60', fg='white', relief=tk.RIDGE)
biscuit_button.grid(row=10, column=0, padx=0, pady=2, ipadx=5, ipady=5)
clear_button = tk.Button(item_frame, text='Clear', command=clear_item, font=('arial', 12, 'bold'), bg='#E74C3C', fg='white', relief=tk.RIDGE)
clear_button.grid(row=10, column=1, padx=5, pady=2,  ipadx=5, ipady=5)

qtn_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qtn_combobox = ttk.Combobox(item_frame, values=qtn_items, state='readonly',width=30)
qtn_combobox.grid(row=7, column=0, padx=10, pady=15)
qtn_combobox.bind('<<ComboboxSelected>>', combobox)
qtn_combobox.set(1)
qtn_button = tk.Button(item_frame, text='Quantity', command=add, font=('arial', 12, 'bold'), bg='#27AE60', fg='white', relief=tk.RIDGE)
qtn_button.grid(row=8, column=0, padx=0, pady=2, ipadx=5, ipady=5)

add_frame = tk.LabelFrame(window, text=' Item detail ', font=('times new roman', 12, 'bold'), bg='black', fg='white', bd=8, relief=tk.RIDGE)
add_frame.pack(side='left', padx=10, pady=10, ipadx=10, ipady=5, anchor="nw")

multiline_text = scrolledtext.ScrolledText(add_frame, width=50, height=35, wrap=tk.WORD, bd=8, relief=tk.RIDGE)
multiline_text.grid(row=2, column=2)

def mainbill():
    customer_name = name_entry.get()
    phone_number = phone_entry.get()
    bill_number = billno_entry.get()

    if not customer_name or not phone_number or not bill_number:
        messagebox.showerror("Error", "Please enter all customer details.")
        return

    bill_date = date.today().strftime("%d/%m/%Y")
    items_and_quantities = multiline_text.get("1.0", tk.END).strip().split('\n')
    total_amount = 0
    cgst = 0
    sgst = 0

    multiline_bill_text.delete("1.0", tk.END)

    multiline_bill_text.insert(tk.END, "--------------------------------------------------\n")
    centered_text = "TAX Invoice\n"
    text_width = 50
    num_spaces = (text_width - len(centered_text)) // 2
    final_text = " " * num_spaces + centered_text + " " * num_spaces
    multiline_bill_text.tag_configure("center", justify='center')
    multiline_bill_text.insert(tk.END, final_text, "center")
    multiline_bill_text.insert(tk.END, f"Bill No. : {bill_number}    \n")
    multiline_bill_text.insert(tk.END, f"Date: {bill_date}    \n")
    multiline_bill_text.insert(tk.END, f"Name: {customer_name}    Phone: {phone_number}\n")
    multiline_bill_text.insert(tk.END, "--------------------------------------------------\n")

    for item_quantity in items_and_quantities:
        item, quantity = item_quantity.split(" - Quantity: ")
        item_parts = item.split("Price")
        item_name = item_parts[0].strip()  # Extract the item name
        item_price = item_parts[1].replace("-", "").strip()  # Extract the item price (remove hyphen and spaces)
        total_item_price = int(item_price) * int(quantity)
        total_amount += total_item_price
        multiline_bill_text.insert(tk.END, f"{item_name} x{quantity} = {total_item_price}\n")

        # Calculate CGST and SGST for each item separately
        cgst_amount = total_item_price * 0.08
        sgst_amount = total_item_price * 0.08
        cgst += cgst_amount
        sgst += sgst_amount

    total_tax = cgst + sgst
    total_amount_with_tax = total_amount + total_tax

    multiline_bill_text.insert(tk.END, "--------------------------------------------------\n")
    multiline_bill_text.insert(tk.END, f"Total Amount (Before Tax): {total_amount}\n")
    multiline_bill_text.insert(tk.END, f"CGST (8%): {cgst}\n")
    multiline_bill_text.insert(tk.END, f"SGST (8%): {sgst}\n")
    multiline_bill_text.insert(tk.END, f"Total Tax: {total_tax}\n")
    multiline_bill_text.insert(tk.END, "--------------------------------------------------\n")
    multiline_bill_text.insert(tk.END, f"Total Amount (After Tax): {total_amount_with_tax}\n")
    multiline_bill_text.insert(tk.END, "--------------------------------------------------\n")
    multiline_bill_text.insert(tk.END, "Thank you for shopping with us!\n")

def clearbill():

    global bill_number
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    multiline_text.delete("1.0", tk.END)
    multiline_bill_text.delete("1.0", tk.END)
    bill_number += 1
    billno_entry.delete(0, tk.END)
    billno_entry.insert(0, str(bill_number))
bill_number = 1




mainbill_frame = tk.LabelFrame(window, text=' Item detail ', font=('times new roman', 12, 'bold'), bg='black', fg='white', bd=8, relief=tk.RIDGE)
mainbill_frame.pack(side='left', padx=10, pady=10, ipadx=20, ipady=20, anchor="nw")
multiline_bill_text = scrolledtext.ScrolledText(mainbill_frame, width=50, height=30, wrap=tk.WORD, bd=8, relief=tk.RIDGE)
multiline_bill_text.grid(row=2, column=0)

mainbill_button = tk.Button(mainbill_frame, text='Generate Bill', command=mainbill, font=('arial', 12, 'bold'), bg='#27AE60', fg='white', relief=tk.RIDGE)
mainbill_button.grid(row=4, column=0, padx=0, pady=2, ipadx=5, ipady=5)
clearbill_button = tk.Button(mainbill_frame, text='Clear Bill', command=clearbill, font=('arial', 12, 'bold'), bg='#27AE60', fg='white', relief=tk.RIDGE)
clearbill_button.grid(row=5, column=0, padx=0, pady=2, ipadx=5, ipady=5)

window.mainloop()
