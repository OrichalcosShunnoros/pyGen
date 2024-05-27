import moviepy.editor
import qrcode
import yt_dlp
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring

def convert_mp4_to_mp3():
    vid = askopenfilename(title="Select MP4 file", filetypes=[("MP4 files", "*.mp4")])
    if vid:
        video = moviepy.editor.VideoFileClip(vid)
        aud = video.audio
        save_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if save_path:
            aud.write_audiofile(save_path)
            print('--- MP3 conversion completed ---')

def download_video():
    url = askstring("Video URL", "Enter video URL:")
    if url:
        ydl_opts = {
            'outtmpl': asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        }
        if ydl_opts['outtmpl']:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print('Video downloaded successfully!')

def generate_qr_code():
    data = askstring("QR Code Data", "Enter the data for the QR code:")
    if data:
        img = qrcode.make(data)
        save_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            img.save(save_path)
            print('--- QR code generated ---')

def download_audio():
    url = askstring("Video URL", "Enter video URL:")
    if not url:
        print("No URL provided. Exiting.")
        return

    save_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not save_path:
        print("No save path provided. Exiting.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': save_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print('Audio downloaded successfully!')

def main():
    root = Tk()
    root.title("Utility Program")

    root.configure(bg="lightblue")

    min_width = 250 
    min_height = 250 
    root.minsize(min_width, min_height)
    root.geometry(f"{min_width}x{min_height}")

    def on_convert_mp4_to_mp3():
        root.destroy()
        convert_mp4_to_mp3()
        main()

    def on_download_video():
        root.destroy()
        download_video()
        main()

    def on_generate_qr_code():
        root.destroy()
        generate_qr_code()
        main()

    def on_download_audio():
        root.destroy()
        download_audio()
        main()

    def on_exit():
        root.destroy()

    Label(root, text="Select an option:", bg="lightblue", font=("Helvetica", 14)).pack(pady=10, fill=X, expand=True)

    Button(root, text="Convert MP4 to MP3", command=on_convert_mp4_to_mp3, bg="white", fg="black").pack(pady=5, padx=20, fill=X, expand=True)
    Button(root, text="Download Video", command=on_download_video, bg="white", fg="black").pack(pady=5, padx=20, fill=X, expand=True)
    Button(root, text="Generate QR Code", command=on_generate_qr_code, bg="white", fg="black").pack(pady=5, padx=20, fill=X, expand=True)
    Button(root, text="Download Audio", command=on_download_audio, bg="white", fg="black").pack(pady=5, padx=20, fill=X, expand=True)
    Button(root, text="Exit", command=on_exit, bg="red", fg="white").pack(pady=5, padx=50, fill=X, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
