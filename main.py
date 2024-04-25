import tkinter
import customtkinter
from pytube import YouTube


#functions
def startDownload():
    try: 
        ytlink = url.get()
        ytObj = YouTube(ytlink)
        vid = ytObj.streams.get_highest_resolution()
        title.configure(text=ytObj.title, text_color="white")
        finishedLabel.configure(text="")
        vid.download()
    except:
        #print("Something went wrong, check the link and Try again...🤷‍♂️")
        finishedLabel.configure(text="Something went wrong, check the link and Try again...🤷‍♂️", text_color="red")
    #print("Download Complete 🥳")
    finishedLabel.configure(text="Download Complete 🥳", text_color="green")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#framework
app = customtkinter.CTk();
app.geometry("720x480")
app.title("PyTube GUI")

#UI Elements
title = customtkinter.CTkLabel(app, text="Insert Youtube URL")
title.pack(padx=10, pady=10)

# url entry box
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Swipe that vid", command=startDownload)
download.pack(padx=10, pady=10)

# Finished Labels
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()


#keep-alive
app.mainloop()

