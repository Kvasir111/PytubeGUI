import tkinter
import customtkinter
from pytube import YouTube


#functions
def startDownload():
    try: 
        ytlink = url.get()
        ytObj = YouTube(ytlink, on_progress_callback=on_progress)
        vid = ytObj.streams.get_highest_resolution()
        title.configure(text=ytObj.title, text_color="white")
        finishedLabel.configure(text="")
        vid.download()
    except:
        #print("Something went wrong, check the link and Try again...🤷‍♂️")
        finishedLabel.configure(text="Something went wrong, check the link and Try again...🤷‍♂️", text_color="red")
    #print("Download Complete 🥳")
    finishedLabel.configure(text="Download Complete 🥳", text_color="green")

def on_progress(stream, chunk, bytes_remaining):
    # Updating Progress % label
    totalVideoSize = stream.filesize
    bytes_downloaded = totalVideoSize - bytes_remaining
    percentageOfCompletion = bytes_downloaded / totalVideoSize * 100
    per = str(int(percentageOfCompletion))
    progress.configure(text=per + "%")
    progress.update()

    # Updating Progress Bar
    progressBar.set(float(percentageOfCompletion/100))

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

# Progress
progress =  customtkinter.CTkLabel(app, text="")
progress.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack()

#keep-alive
app.mainloop()

