import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress
import threading
import os

DESTINO = "videos"

def baixar_video():
    url = entrada_url.get()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return

    def processo_download():
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

            if not os.path.exists(DESTINO):
                os.makedirs(DESTINO)

            status.set("Baixando...")
            stream.download(output_path=DESTINO)
            status.set("Download concluído!")
        except Exception as e:
            status.set("Erro no download.")
            messagebox.showerror("Erro", str(e))

    threading.Thread(target=processo_download).start()


janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("400x170")

tk.Label(janela, text="URL do vídeo do YouTube:").pack(pady=10)

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack()

tk.Button(janela, text="Baixar", command=baixar_video).pack(pady=10)

status = tk.StringVar()
tk.Label(janela, textvariable=status).pack()

tk.Button(janela, text="Cancelar", command=janela.destroy).pack(pady=10)

janela.mainloop()
