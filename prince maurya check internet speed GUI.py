from tkinter import *
import speedtest as s

window = Tk()
window.title("Prince Maurya")
window.geometry("790x400+600+100")
window.config(bg="#29e6f1")

f1 = Frame(window)
result = Frame(window)

Label(f1, text="Prince Maurya, Internet Speed Test", font=("Times", 30, "bold"), bg="blue", fg="#2bf814").pack(side=TOP)

a = Label(result, text="Processing...", font=("Time New Roman", 20, "bold"), bg="#e6e6e6", fg="black")
a.pack(side=TOP)
a.grid_forget()
txt = Text(result, font=("Times", 15, "bold"), bg="white", fg="black", padx=30, pady=20)


def text_search():
    a.grid_forget()
    obj = s.Speedtest()
    download_speed = obj.download() / 1000000
    upload_speed = obj.upload() / 1000000
    txt.pack()
    txt.insert(END, f"Downloading speed : {download_speed:.2f} Mbps\n")
    txt.insert(END, f"Uploading speed      : {upload_speed:.2f} Mbps\n")

    a.grid()
btn1 = Button(f1, text="Test Speed", command=text_search, font=("Time New Roman", 15, "bold"), bg="#e6e6e6", fg="black")
btn1.pack(side=RIGHT)

f1.pack(side=TOP)
result.pack(side=TOP, padx=55, pady=20)

window.mainloop()
