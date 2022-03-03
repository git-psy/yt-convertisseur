import youtube_dl
from pytube import YouTube
from tkinter import *

"""
Ce code permet de telecharger des videos/musiques depuis youtube...
"""

#variable de couleurs
bg="#373737"
fg="orange"

#creation de la fenetre
root=Tk()
root.withdraw()
screen = Toplevel(root)

screen.title("Youtube - converter to mp3/mp4")
screen['bg']=bg
screen.geometry("500x400+500+100")
screen.resizable(False, False)

def quit_screen():
    root.destroy()

screen.protocol("WM_DELETE_WINDOW", quit_screen)

#text: "Convertisseur Yt"
title=Label(screen ,text="Convertisseur Yt",bg=bg , fg=fg, font=("Arial", 30))
title.pack()

def url_return(event):
    try:
        yt = YouTube(url_entry.get())
        name_entry.delete(0, "end")
        name_entry.insert(0, yt.title)
    except:
        name_entry.delete(0, "end")
        name_entry.insert(0, "Erreur: Url inexistante")

frame_url = Frame(screen, bg=bg)
frame_url.pack(pady=5, padx=5)
url_label=Label(frame_url ,text="Lien : (touche Entrée pour charger le nom)",bg=bg , fg=fg, font=("Arial", 13))
url_label.pack(side=TOP)
url_entry = Entry(frame_url, insertbackground="orange", width=45, background=bg, foreground=fg, highlightcolor=fg, highlightbackground=fg)
url_entry.pack(side=BOTTOM)
url_entry.bind("<Return>", url_return)
url_entry.focus()

frame_name = Frame(screen, bg=bg)
frame_name.pack(pady=5,padx=5)
name_label=Label(frame_name ,text="Nom : ",bg=bg , fg=fg, font=("Arial", 13))
name_label.pack(side=TOP)
name_entry = Entry(frame_name, insertbackground="orange", width=45, background=bg, foreground=fg, highlightcolor=fg, highlightbackground=fg)
name_entry.pack(side=BOTTOM)

format = StringVar()
format.set("mp3")

mp3 = Radiobutton(
    screen,
    activeforeground=fg,
    foreground=fg,
    highlightbackground=bg,
    activebackground=bg,
    text="musique: mp3",
    variable=format,
    value="mp3",
    font="arial 20",
    bg=bg)
mp3.pack(anchor="s")

mp4 = Radiobutton(
    screen,
    activeforeground=fg,
    foreground=fg,
    highlightbackground=bg,
    activebackground=bg,
    text="video : mp4",
    variable=format,
    value="mp4",
    font="arial 20",
    bg=bg)
mp4.pack(anchor="s")

def download():
    try:
        text["text"] = "Telechargement..."
        yt = YouTube(url_entry.get())
        if format.get() == "mp3":
            yt = yt.streams.get_audio_only()
            yt.download(output_path="Download", filename=f"{name_entry.get()}.mp3")
            text["text"] = "Telechargement terminé"
        else:
            yt = yt.streams.get_highest_resolution()
            yt.download(output_path="Download", filename=f"{name_entry.get()}.mp4")
            text["text"] = "Telechargement terminé"
    except:
        text["text"]="L'url est invalide"

dwn_btn=Button(screen, text="Télécharger", cursor="dot", command=download, background=bg, foreground=fg, activeforeground=bg, activebackground=fg, highlightbackground=fg, borderwidth=3)
dwn_btn.pack(pady=30)

text=Label(screen ,text="",bg=bg , fg=fg, font=("Arial", 13))
text.pack()

screen.mainloop()
