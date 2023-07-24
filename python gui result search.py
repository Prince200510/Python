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

from tkinter import *
import wikipedia as wk
import pyttsx3
from reportlab.pdfgen import canvas
from tkinter import filedialog
from tkinter import messagebox
import textwrap
from reportlab.lib import colors
window = Tk()
window.title("Prince Maurya")
window.geometry("790x800+600+100")
window.resizable(False, False)
window.config(bg="#29e6f1")
f1 = Frame(window)
result = Frame(window)
Label(f1,text="Prince Maurya, Search Result",font=("Times",30,"bold"),bg="blue",fg="#2bf814").pack(side=TOP)
Label(f1,text="Search",font=("Time New Roman",20,"bold"),bg="yellow",fg="black").pack(side=LEFT)
Label(result,text="Search Result...",font=("Time New Roman",20,"bold"),bg="#e6e6e6",fg="black").pack(side=TOP)
entry_box = Entry(f1,width="30",font=("Time New Roman",15),bg="#e6e6e6",fg="black")
entry_box.pack(side=TOP)
txt  = Text(result,font=("Times",15,"bold"),bg="white",fg="black",padx=30,pady=20)
def text_search():
    global seat_number
    names = ["prince maurya", "Harsh Maurya", "Krishna        ","Aaryan       ","Shivam       "]
    index = 1
    name = names[index]
    seat_number = entry_box.get()
    if seat_number == "1001":
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"                                                Result 2023-24 PT-1              \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        index = 0
        name = names[index]
        txt.insert(END, "Name    : " + name + "                                                          Seat No : 1001 \n")
        txt.insert(END, "Institue : Thakur Polytechnic                        Enrollement No : 2105220374 \n")
        txt.insert(END, "Programme : Diploma in Computer Engineering \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"   |--------------------------------------------------------| \n")
        txt.insert(END,"  | Title of courses  |                    Marks                  |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END,"  |                             |   MAX.    |   MIN.   |   OBT.    |\n ")
        txt.insert(END," |--------------------------------------------------------| \n")
        txt.insert(END,"  | MIC                    |       20      |     08      |     19       |\n")
        txt.insert(END,"  | DCC                   |       20      |     08      |     17       |\n")
        txt.insert(END,"  | SEN                    |       20      |     08      |     15       |\n")
        txt.insert(END,"  | JPR                    |       20      |     08      |     20       |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END," TOTAL MARKS : 80 / 71             PERC. :  88.75\n")
        txt.insert(END," PASS WITH        : FIRST CLASS DIST.             \n")
        txt.insert(END,"--------------------------------------------------------------------------------------")
    elif seat_number == "1002":
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"                                                Result 2023-24 PT-1              \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        index = 1
        name = names[index]
        txt.insert(END, "Name    : " + name + "                                                          Seat No : 1001 \n")
        txt.insert(END, "Institue : Thakur Polytechnic                        Enrollement No : 2105220374 \n")
        txt.insert(END, "Programme : Diploma in Computer Engineering \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"   |--------------------------------------------------------| \n")
        txt.insert(END,"  | Title of courses  |                    Marks                  |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END,"  |                             |   MAX.    |   MIN.   |   OBT.    |\n ")
        txt.insert(END," |--------------------------------------------------------| \n")
        txt.insert(END,"  | MIC                    |       20      |     08      |     19       |\n")
        txt.insert(END,"  | DCC                   |       20      |     08      |     07       |\n")
        txt.insert(END,"  | SEN                    |       20      |     08      |     05       |\n")
        txt.insert(END,"  | JPR                    |       20      |     08      |     20       |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END," TOTAL MARKS : 80 / 51             PERC. :  63.75\n")
        txt.insert(END," PASS WITH        : FIRST CLASS.             \n")
        txt.insert(END,"--------------------------------------------------------------------------------------")
    elif seat_number == "1003":
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"                                                Result 2023-24 PT-1              \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        index = 2
        name = names[index]
        txt.insert(END, "Name    : " + name + "                                                          Seat No : 1001 \n")
        txt.insert(END, "Institue : Thakur Polytechnic                        Enrollement No : 2105220374 \n")
        txt.insert(END, "Programme : Diploma in Computer Engineering \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"   |--------------------------------------------------------| \n")
        txt.insert(END,"  | Title of courses  |                    Marks                  |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END,"  |                             |   MAX.    |   MIN.   |   OBT.    |\n ")
        txt.insert(END," |--------------------------------------------------------| \n")
        txt.insert(END,"  | MIC                    |       20      |     08      |     05       |\n")
        txt.insert(END,"  | DCC                   |       20      |     08      |     07       |\n")
        txt.insert(END,"  | SEN                    |       20      |     08      |     04       |\n")
        txt.insert(END,"  | JPR                    |       20      |     08      |     19       |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END," TOTAL MARKS : 80 / 35             PERC. :  43.75\n")
        txt.insert(END," PASS WITH        : PASS.             \n")
        txt.insert(END,"--------------------------------------------------------------------------------------")
    elif seat_number == "1004":
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"                                                Result 2023-24 PT-1              \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        index = 3
        name = names[index]
        txt.insert(END, "Name    : " + name + "                                                          Seat No : 1001 \n")
        txt.insert(END, "Institue : Thakur Polytechnic                        Enrollement No : 2105220374 \n")
        txt.insert(END, "Programme : Diploma in Computer Engineering \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"   |--------------------------------------------------------| \n")
        txt.insert(END,"  | Title of courses  |                    Marks                  |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END,"  |                             |   MAX.    |   MIN.   |   OBT.    |\n ")
        txt.insert(END," |--------------------------------------------------------| \n")
        txt.insert(END,"  | MIC                    |       20      |     08      |     08       |\n")
        txt.insert(END,"  | DCC                   |       20      |     08      |     10       |\n")
        txt.insert(END,"  | SEN                    |       20      |     08      |     11       |\n")
        txt.insert(END,"  | JPR                    |       20      |     08      |     13       |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END," TOTAL MARKS : 80 / 42             PERC. :  52.05\n")
        txt.insert(END," PASS WITH        : SECOND CLASS.             \n")
        txt.insert(END,"--------------------------------------------------------------------------------------")
    elif seat_number == "1005":
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"                                                Result 2023-24 PT-1              \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        index = 4
        name = names[index]
        txt.insert(END, "Name    : " + name + "                                                          Seat No : 1001 \n")
        txt.insert(END, "Institue : Thakur Polytechnic                        Enrollement No : 2105220374 \n")
        txt.insert(END, "Programme : Diploma in Computer Engineering \n")
        txt.insert(END,"----------------------------------------------------------------------------------------")
        txt.insert(END,"   |--------------------------------------------------------| \n")
        txt.insert(END,"  | Title of courses  |                    Marks                  |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END,"  |                             |   MAX.    |   MIN.   |   OBT.    |\n ")
        txt.insert(END," |--------------------------------------------------------| \n")
        txt.insert(END,"  | MIC                    |       20      |     08      |     14       |\n")
        txt.insert(END,"  | DCC                   |       20      |     08      |     08       |\n")
        txt.insert(END,"  | SEN                    |       20      |     08      |     19       |\n")
        txt.insert(END,"  | JPR                    |       20      |     08      |     16       |\n")
        txt.insert(END,"  |--------------------------------------------------------| \n")
        txt.insert(END," TOTAL MARKS : 80 / 57             PERC. :  71.25\n")
        txt.insert(END," PASS WITH        : FIRST CLASS.             \n")
        txt.insert(END,"--------------------------------------------------------------------------------------")
    else:
        txt.insert(END, "Result not found...")
def cancel():
    entry_box.delete(0, 'end')
def clear_screen():
    txt.delete("1.0", END)
def generate_pdf():
    result_text = txt.get("1.0", END)
    directory = filedialog.askdirectory()
    if directory:
        pdf_file = directory + "/result.pdf"
        c = canvas.Canvas(pdf_file)
        font_name = "Helvetica"
        font_size = 12
        c.setFont(font_name, font_size)
        textbox_width = 1060
        textbox_height = 20
        lines = result_text.split("\n")
        y = 800
        for line in lines:
            wrapped_lines = textwrap.wrap(line, width=textbox_width // font_size)
            for wrapped_line in wrapped_lines:
                c.drawString(30, y, wrapped_line)
                y -= textbox_height
        c.save()
        txt.insert(END, "\nPDF saved as: " + pdf_file)
        messagebox.showinfo("Success", "PDF saved successfully!")
    else:
        messagebox.showwarning("Warning", "No destination directory selected!")

btn_pdf = Button(f1, text="Download PDF", command=generate_pdf, font=("Time New Roman", 15, "bold"), bg="#e6e6e6",
                 fg="black")
btn_pdf.pack(side=RIGHT)
btn3 = Button(f1,text="Clear screen",command=clear_screen,font=("Time New Roman",15,"bold"),bg="#e6e6e6",fg="black")
btn3.pack(side=RIGHT)
btn2 = Button(f1,text="Cancel",command=cancel,font=("Time New Roman",15,"bold"),bg="#e6e6e6",fg="black")
btn2.pack(side=RIGHT)
btn1 = Button(f1,text="Search",command=text_search,font=("Time New Roman",15,"bold"),bg="#e6e6e6",fg="black")
btn1.pack(side=RIGHT)

f1.pack(side=TOP)
result.pack(side=TOP, padx=55,pady=20)
txt.pack()
window.mainloop()