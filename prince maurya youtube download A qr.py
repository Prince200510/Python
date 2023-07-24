#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prince
#
# Created:     14-07-2023
# Copyright:   (c) prince 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import qrcode
from pytube import YouTube
from tkinter import Tk, filedialog
import os


print("===============================================================")
print("                    Download YouTube Video                     ")
print("===============================================================")
print("For downloading a YouTube video, follow the following steps:")
print("Step 1: Select the folder or path where to save the video file.")
print("Step 2: Paste the URL of the video.")
print("Step 3: Done! Check the selected path or folder from Step 1.")
print("===============================================================")

root = Tk()
root.withdraw()
folder = filedialog.askdirectory(title="Select Folder to Save the Video")

if folder:
    url = input("Enter the URL: ")
    try:
        yt = YouTube(url)
        yt.streams.first().download(output_path=folder)
        print("Video downloaded successfully!")

        a = input("Download the QR code for this link? (y/n): ")
        if a.lower() == "y":
            qr = qrcode.QRCode()
            qr.add_data(url)
            qr.make(fit=True)

            qr_code_filename = os.path.join(folder, "prince maurya.png")
            qr.make_image(fill_color="black", back_color="white").save(qr_code_filename)
            print("QR code generated successfully!")
        else:
            print("QR not downloaded")

    except Exception as e:
        print("Error occurred. Video not downloaded:", str(e))

else:
    print("No folder selected. Download canceled.")
