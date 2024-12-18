from pytube import YouTube
import os
import tkinter as tk
from tkinter import ttk , filedialog , messagebox

def download_video():
    url = url_entry.get()
    save_path = save_path_entry.get()
    if not url or not save_path:
        messagebox.showwarning("Input Error" , "please provide a vaild URL and save path")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_hights_resolution()
        messagebox.showinfo("Dowenload" , f"Dowenload video : {yt.title}")
        stream.dowenload(save_path)
        messagebox.showinfo("Success" , " video downloaded successfully!")
    except Exception as e :
        messagebox.showerror("Error" , f"An error occurred : {e}")

def download_audio():
    url = url_entry.get()
    save_path = save_path_entry.get()
    if not url or not save_path:
        messagebox.showwarning("Input Error" , "Please provide a vaild URL and save path .")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio = True).firest()
        messagebox.showinfo("Dowinloading" , f"Downloading audio:  {yt.title}")
        stream.download(save_path , filename = f"{yt.titel}.mp3")
        messagebox.showinfo("Success" , "Audio dowenload successfully!")
    except Exception as e:
        messagebox.showerror("Error" , f"An error occurred : {e}")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, folder)

root = tk.Tk()
root.title("Youtube Dowenloader")
root.geometry("500x250")
root.register(False, False)

tk.Label(root , text="YouTube URL :").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root , text="Save Path :").pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=5)
save_path_entry = tk.Entry(frame , width=40)
save_path_entry.pack(side=tk.LEFT , padx=5)
browser_button = ttk.Button(frame , text="Browse" , command=browse_folder)
browser_button.pack(side=tk.LEFT)


video_button = ttk.Button(root , text="Download video" , command=download_video)
video_button.pack(pady=10)

audio_button = ttk.Button(root ,text="Download Audio" , command=download_audio)
audio_button.pack(pady=10)

root.mainloop()