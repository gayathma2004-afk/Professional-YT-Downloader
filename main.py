import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import yt_dlp
import os

def download_media():
    url = url_entry.get()
    choice = download_choice.get()
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid YouTube URL!")
        return

    save_path = filedialog.askdirectory()
    if not save_path:
        return

    if choice == "Audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }

    try:
        status_label.config(text="Status: Download in progress...", foreground="#3498db")
        root.update_idletasks()
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        status_label.config(text="Status: Download Completed! ✅", foreground="#27ae60")
        messagebox.showinfo("Success", "Media downloaded successfully!")
    except Exception as e:
        status_label.config(text="Status: Error Occurred!", foreground="#e74c3c")
        messagebox.showerror("Error", f"Failed to download: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Python YT Downloader Pro")
root.geometry("500x450")
root.configure(bg="#f0f3f5") # Light Gray background

# Header Section
header_frame = tk.Frame(root, bg="#c4302b", height=80)
header_frame.pack(fill="x")

tk.Label(header_frame, text="YouTube Downloader", font=("Segoe UI", 20, "bold"), fg="white", bg="#c4302b").pack(pady=20)

# Main Container
container = tk.Frame(root, bg="#f0f3f5", padx=30, pady=20)
container.pack(expand=True, fill="both")

# URL Input
tk.Label(container, text="Paste Video Link Here:", font=("Segoe UI", 11), bg="#f0f3f5").pack(anchor="w")
url_entry = tk.Entry(container, width=50, font=("Segoe UI", 10), bd=2, relief="flat")
url_entry.pack(pady=10, ipady=5)

# Style for Radiobuttons
style = ttk.Style()
style.configure("TFrame", background="#f0f3f5")

# Format Selection Section
choice_frame = tk.LabelFrame(container, text=" Select Download Format ", font=("Segoe UI", 10, "bold"), bg="#f0f3f5", padx=20, pady=10)
choice_frame.pack(pady=20, fill="x")

download_choice = tk.StringVar(value="Video")
tk.Radiobutton(choice_frame, text="Video (MP4)", variable=download_choice, value="Video", bg="#f0f3f5", font=("Segoe UI", 10)).pack(side="left", padx=20)
tk.Radiobutton(choice_frame, text="Audio Only (MP3)", variable=download_choice, value="Audio", bg="#f0f3f5", font=("Segoe UI", 10)).pack(side="left", padx=20)

# Modern Download Button
download_btn = tk.Button(container, text="START DOWNLOAD", command=download_media, 
                         bg="#c4302b", fg="white", font=("Segoe UI", 12, "bold"), 
                         relief="flat", cursor="hand2", activebackground="#a32824", activeforeground="white")
download_btn.pack(pady=10, fill="x", ipady=10)

# Footer Status
status_label = tk.Label(root, text="System Ready", font=("Segoe UI", 9, "italic"), bg="#f0f3f5", fg="#7f8c8d")
status_label.pack(side="bottom", pady=10)

root.mainloop()