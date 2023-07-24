#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prince
#
# Created:     17-07-2023
# Copyright:   (c) prince 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import qrcode
from tkinter import *
from tkinter import filedialog
import urllib.request
from tkinter import messagebox
from PIL import Image, ImageTk
import textwrap
from reportlab.lib import colors
from reportlab.pdfgen import canvas
window = Tk()
window.title("Prince Maurya")
window.geometry("790x400+600+100")
window.config(bg="#29e6f1")

f1 = Frame(window)
result = Frame(window)

Label(f1, text="Prince Maurya, QR Generator", font=("Times", 30, "bold"), bg="blue", fg="#2bf814").pack(side=TOP)
Label(f1, text="Enter the Link", font=("Time New Roman", 20, "bold"), bg="yellow", fg="black").pack(side=LEFT)
Label(result, text="QR Generating...", font=("Time New Roman", 20, "bold"), bg="#e6e6e6", fg="black").pack(side=TOP)

entry_box = Entry(f1, width="30", font=("Time New Roman", 15), bg="#e6e6e6", fg="black")
entry_box.pack(side=TOP)

txt = Text(result, font=("Times", 15, "bold"), bg="white", fg="black", padx=30, pady=20)


def text_search():
    link = entry_box.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qr_code.png")  # Save the QR code image to a file
    qr_image = ImageTk.PhotoImage(Image.open("qr_code.png"))
    txt = Label(result, image=qr_image)
    txt.image=qr_image
    txt.pack()
    txt.insert(END, "\nQR Code generated successfully!\n")
    txt.insert(END, "Download the QR code using the button below.\n")

def cancel():
    entry_box.delete(0, 'end')

def download_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    link = entry_box.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_path)
    txt.insert(END, f"QR Code saved successfully at:\n{file_path}\n")

    


btn2 = Button(f1, text="Cancel", command=cancel, font=("Time New Roman", 15, "bold"), bg="#e6e6e6", fg="black")
btn2.pack(side=RIGHT)

btn1 = Button(f1, text="Generate QR", command=text_search, font=("Time New Roman", 15, "bold"), bg="#e6e6e6", fg="black")
btn1.pack(side=RIGHT)

download_btn = Button(result, text="Download QR", command=download_qr, font=("Time New Roman", 15, "bold"),
                      bg="#e6e6e6", fg="black")
download_btn.pack(side=BOTTOM)

f1.pack(side=TOP)
result.pack(side=TOP, padx=55, pady=20)

window.mainloop()

