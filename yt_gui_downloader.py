from __future__ import annotations
import re
import subprocess
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
import webbrowser
import sys
import os

# Optional: use ttkbootstrap if available for better-looking UI
try:
    import ttkbootstrap as tb
    THEME = "darkly"
    use_bootstrap = True
except ImportError:
    tb = ttk
    use_bootstrap = False
    THEME = None


class DownloaderGUI:
    def __init__(self):
        # Built-in language dictionary for dynamic language switching
        self.languages = {
            "en": {
                "title": "YT Downloader | €fendi",
                "file": "File",
                "exit": "Exit",
                "settings": "Settings",
                "create_playlist_folder": "Create playlist folder",
                "theme": "Theme",
                "light": "Light",
                "dark": "Dark",
                "help": "Help",
                "about": "About",
                "url": "YouTube URL",
                "folder": "Save Folder",
                "browse": "Browse",
                "type": "Download Type",
                "video": "Video",
                "audio": "Audio",
                "resolution": "Resolution",
                "format": "Format",
                "download": "Download",
                "cookies": "Upload YouTube login cookie file:",
                "select_cookie": "Select cookies.txt",
                "selected_file": "Selected file:",
                "version": "Beta v0.1.1",
                "powered": "Powered by €fendi",
                "github": "GitHub",
                "done": "✅ Download complete",
                "error": "Error",
                "no_url": "URL is missing"
            },
            "tr": {
                "title": "YT Downloader | €fendi",
                "file": "Dosya",
                "exit": "Çıkış",
                "settings": "Ayarlar",
                "create_playlist_folder": "Playlist klasörü oluştur",
                "theme": "Tema",
                "light": "Açık",
                "dark": "Koyu",
                "help": "Yardım",
                "about": "Hakkında",
                "url": "YouTube URL",
                "folder": "Kayıt Klasörü",
                "browse": "Gözat",
                "type": "İndirme Türü",
                "video": "Video",
                "audio": "Ses",
                "resolution": "Çözünürlük",
                "format": "Format",
                "download": "İndir",
                "cookies": "YouTube girişli çerez dosyasını yükle:",
                "select_cookie": "cookies.txt Seç",
                "selected_file": "Seçili dosya:",
                "version": "Beta v0.1.1",
                "powered": "Powered by €fendi",
                "github": "GitHub",
                "done": "✅ İndirme tamamlandı",
                "error": "Hata",
                "no_url": "URL girilmedi"
            },
            "fr": {
                "title": "Téléchargeur YT | €fendi",
                "file": "Fichier",
                "exit": "Quitter",
                "settings": "Paramètres",
                "create_playlist_folder": "Créer un dossier de playlist",
                "theme": "Thème",
                "light": "Clair",
                "dark": "Sombre",
                "help": "Aide",
                "about": "À propos",
                "url": "URL YouTube",
                "folder": "Dossier de destination",
                "browse": "Parcourir",
                "type": "Type de téléchargement",
                "video": "Vidéo",
                "audio": "Audio",
                "resolution": "Résolution",
                "format": "Format",
                "download": "Télécharger",
                "cookies": "Charger le fichier cookies.txt connecté à YouTube:",
                "select_cookie": "Sélectionner cookies.txt",
                "selected_file": "Fichier sélectionné:",
                "version": "Beta v0.1.1",
                "powered": "Propulsé par €fendi",
                "github": "GitHub",
                "done": "✅ Téléchargement terminé",
                "error": "Erreur",
                "no_url": "URL manquante"
            },
            "de": {
                "title": "YT Downloader | €fendi",
                "file": "Datei",
                "exit": "Beenden",
                "settings": "Einstellungen",
                "create_playlist_folder": "Playlist-Ordner erstellen",
                "theme": "Thema",
                "light": "Hell",
                "dark": "Dunkel",
                "help": "Hilfe",
                "about": "Über",
                "url": "YouTube-URL",
                "folder": "Zielordner",
                "browse": "Durchsuchen",
                "type": "Download-Typ",
                "video": "Video",
                "audio": "Audio",
                "resolution": "Auflösung",
                "format": "Format",
                "download": "Herunterladen",
                "cookies": "YouTube-Cookie-Datei laden:",
                "select_cookie": "cookies.txt auswählen",
                "selected_file": "Ausgewählte Datei:",
                "version": "Beta v0.1.1",
                "powered": "Bereitgestellt von €fendi",
                "github": "GitHub",
                "done": "✅ Download abgeschlossen",
                "error": "Fehler",
                "no_url": "URL fehlt"
            },
            "es": {
                "title": "Descargador YT | €fendi",
                "file": "Archivo",
                "exit": "Salir",
                "settings": "Configuraciones",
                "create_playlist_folder": "Crear carpeta de lista",
                "theme": "Tema",
                "light": "Claro",
                "dark": "Oscuro",
                "help": "Ayuda",
                "about": "Acerca de",
                "url": "URL de YouTube",
                "folder": "Carpeta de guardado",
                "browse": "Explorar",
                "type": "Tipo de descarga",
                "video": "Vídeo",
                "audio": "Audio",
                "resolution": "Resolución",
                "format": "Formato",
                "download": "Descargar",
                "cookies": "Sube archivo de cookies de YouTube:",
                "select_cookie": "Seleccionar cookies.txt",
                "selected_file": "Archivo seleccionado:",
                "version": "Beta v0.1.1",
                "powered": "Desarrollado por €fendi",
                "github": "GitHub",
                "done": "✅ Descarga completada",
                "error": "Error",
                "no_url": "Falta la URL"
            },
            "pt": {
                "title": "YT Downloader | €fendi",
                "file": "Arquivo",
                "exit": "Sair",
                "settings": "Configurações",
                "create_playlist_folder": "Criar pasta da playlist",
                "theme": "Tema",
                "light": "Claro",
                "dark": "Escuro",
                "help": "Ajuda",
                "about": "Sobre",
                "url": "URL do YouTube",
                "folder": "Pasta de destino",
                "browse": "Procurar",
                "type": "Tipo de download",
                "video": "Vídeo",
                "audio": "Áudio",
                "resolution": "Resolução",
                "format": "Formato",
                "download": "Baixar",
                "cookies": "Carregar arquivo cookies.txt do YouTube:",
                "select_cookie": "Selecionar cookies.txt",
                "selected_file": "Arquivo selecionado:",
                "version": "Beta v0.1.1",
                "powered": "Desenvolvido por €fendi",
                "github": "GitHub",
                "done": "✅ Download concluído",
                "error": "Erro",
                "no_url": "URL não fornecida"
            }
        }

        self.lang_code = "en"  # Default language is English
        self.root = tb.Window(themename=THEME) if use_bootstrap else tk.Tk()
        self._build_interface()
        self.root.mainloop()

    # Translate label/key based on active language
    def t(self, key):
        return self.languages.get(self.lang_code, {}).get(key, key)

    # Initial UI build
    def _build_interface(self):
        self.root.title(self.t("title"))
        self.root.geometry("820x520")
        self.root.minsize(720, 460)

        self.output_dir = tk.StringVar(value=str(Path.cwd()))
        self.cookies_path = tk.StringVar()
        self.create_playlist_folder = tk.BooleanVar(value=True)

        self._build_menu()
        self._build_tabs()

    # Build top menu
    def _build_menu(self):
        mbar = tk.Menu(self.root)
        self.root.config(menu=mbar)

        # File menu
        file_m = tk.Menu(mbar, tearoff=0)
        file_m.add_command(label=self.t("exit"), command=self.root.quit)
        mbar.add_cascade(label=self.t("file"), menu=file_m)

        # Settings menu
        settings_m = tk.Menu(mbar, tearoff=0)
        settings_m.add_checkbutton(label=self.t("create_playlist_folder"), variable=self.create_playlist_folder)

        # Language menu
        lang_m = tk.Menu(settings_m, tearoff=0)
        for code in self.languages:
            lang_m.add_command(label=code.upper(), command=lambda c=code: self._change_language(c))
        settings_m.add_cascade(label="Language", menu=lang_m)

        mbar.add_cascade(label=self.t("settings"), menu=settings_m)

        # Theme menu (only available with ttkbootstrap)
        if use_bootstrap:
            theme_m = tk.Menu(mbar, tearoff=0)
            theme_m.add_command(label=self.t("light"), command=lambda: self.root.style.theme_use("flatly"))
            theme_m.add_command(label=self.t("dark"), command=lambda: self.root.style.theme_use("darkly"))
            mbar.add_cascade(label=self.t("theme"), menu=theme_m)

        # Help menu
        help_m = tk.Menu(mbar, tearoff=0)
        help_m.add_command(label=self.t("about"), command=self._show_about)
        mbar.add_cascade(label=self.t("help"), menu=help_m)

    # Create the tab views
    def _build_tabs(self):
        nb = ttk.Notebook(self.root)
        nb.pack(fill="both", expand=True)

        self.single_tab = ttk.Frame(nb)
        self.play_tab = ttk.Frame(nb)
        self.cookie_tab = ttk.Frame(nb)

        nb.add(self.single_tab, text="Single Video")
        nb.add(self.play_tab, text="Playlist")
        nb.add(self.cookie_tab, text="Cookies")

        self._build_tab_ui(self.single_tab, playlist=False)
        self._build_tab_ui(self.play_tab, playlist=True)
        self._build_cookie_tab(self.cookie_tab)

    # Handle dynamic language switch and rebuild UI
    def _change_language(self, code):
        self.lang_code = code
        for widget in self.root.winfo_children():
            widget.destroy()
        self._build_interface()

    # Build one tab's UI elements (used for both single video and playlist)
    def _build_tab_ui(self, frame: ttk.Frame, playlist: bool):
        r = 0
        ttk.Label(frame, text=self.t("url")).grid(row=r, column=0, sticky="w", padx=10, pady=5)
        url = tk.StringVar()
        ttk.Entry(frame, textvariable=url, width=90).grid(row=r, column=1, columnspan=4, sticky="w")

        r += 1
        ttk.Label(frame, text=self.t("folder")).grid(row=r, column=0, sticky="w", padx=10)
        ttk.Entry(frame, textvariable=self.output_dir, width=65).grid(row=r, column=1, sticky="w")
        ttk.Button(frame, text=self.t("browse"), command=self.choose_folder).grid(row=r, column=2, sticky="w")

        r += 1
        ttk.Label(frame, text=self.t("type")).grid(row=r, column=0, sticky="w", padx=10)
        mode = tk.StringVar(value="video")
        ttk.Radiobutton(frame, text=self.t("video"), variable=mode, value="video").grid(row=r, column=1, sticky="w")
        ttk.Radiobutton(frame, text=self.t("audio"), variable=mode, value="audio").grid(row=r, column=2, sticky="w")

        r += 1
        ttk.Label(frame, text=self.t("resolution")).grid(row=r, column=0, sticky="w", padx=10)
        res = tk.StringVar(value="720")
        ttk.Combobox(frame, values=["Auto", "1080", "720", "480", "360"], textvariable=res, width=10, state="readonly").grid(row=r, column=1, sticky="w")
        ttk.Label(frame, text=self.t("format")).grid(row=r, column=2, sticky="w")
        fmt = tk.StringVar(value="mp4")
        ttk.Combobox(frame, values=["mp4", "mkv", "webm", "mp3", "m4a"], textvariable=fmt, width=10, state="readonly").grid(row=r, column=3, sticky="w")

        r += 1
        prog = ttk.Progressbar(frame, orient="horizontal", mode="determinate")
        prog.grid(row=r, column=0, columnspan=5, sticky="ew", padx=10, pady=5)

        r += 1
        log = tk.Text(frame, height=10)
        log.grid(row=r, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

        r += 1
        ttk.Button(frame, text=self.t("download"), command=lambda: self.start_download(url.get().strip(), not playlist, mode.get(), res.get(), fmt.get(), prog, log)).grid(row=r, column=2, pady=5)

        frame.grid_rowconfigure(r - 1, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    # Cookie tab UI
    def _build_cookie_tab(self, frame):
        ttk.Label(frame, text=self.t("cookies"), font=("Segoe UI", 11)).pack(pady=10)
        ttk.Button(frame, text=self.t("select_cookie"), command=self._select_cookie_file).pack(pady=10)
        self.cookie_path_label = ttk.Label(frame, text=f"{self.t('selected_file')} (none)", foreground="gray")
        self.cookie_path_label.pack()

    # Cookie file selector
    def _select_cookie_file(self):
        file = filedialog.askopenfilename(title=self.t("select_cookie"), filetypes=[("Text files", "*.txt")])
        if file:
            self.cookies_path.set(file)
            self.cookie_path_label.config(text=f"{self.t('selected_file')} {file}", foreground="green")

    # About popup window
    def _show_about(self):
        win = tk.Toplevel(self.root)
        win.title(self.t("about"))
        ttk.Label(win, text=f"{self.t('title')} {self.t('version')}", font=("Segoe UI", 20, "bold")).pack(pady=5)
        ttk.Label(win, text=self.t("powered")).pack(pady=5)
        link = ttk.Label(win, text=self.t("github") + ": https://github.com/emirhankaymakc1", foreground="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/emirhankaymakc1"))

    # Choose folder handler
    def choose_folder(self):
        d = filedialog.askdirectory()
        if d:
            self.output_dir.set(d)

    # Start download thread
    def start_download(self, url: str, single: bool, mode: str, res: str, fmt: str, pb: ttk.Progressbar, log: tk.Text):
        if not url:
            messagebox.showerror(self.t("error"), self.t("no_url"))
            return
        pb["value"] = 0
        threading.Thread(target=self.download_thread, args=(url, single, mode, res, fmt, pb, log), daemon=True).start()

    # Download process and output capture
    def download_thread(self, url: str, single: bool, mode: str, res: str, fmt: str, pb: ttk.Progressbar, log: tk.Text):
        base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
        os.environ["PATH"] += os.pathsep + os.path.join(base_path, "ffmpeg")
        yt_dlp_path = os.path.join(os.path.dirname(__file__), "yt-dlp.exe")

        out_dir = Path(self.output_dir.get())
        tmpl = "%(title)s.%(ext)s" if not self.create_playlist_folder.get() else "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s"
        out_tpl = str(out_dir / tmpl)

        if mode == "video":
            h = "" if res == "Auto" else f"[height<={res}]"
            fstr = f"bestvideo[ext=mp4]{h}+bestaudio[ext=m4a]/best[ext=mp4]{h}"
        else:
            fstr = "bestaudio[ext=m4a]/bestaudio"
            fmt = fmt if fmt in ("mp3", "m4a") else "m4a"

        cmd = [yt_dlp_path, url, "-f", fstr, "-o", out_tpl, "--newline"]
        if single:
            cmd.append("--no-playlist")
        if self.cookies_path.get():
            cmd += ["--cookies", self.cookies_path.get()]
        if mode == "video":
            cmd += ["--merge-output-format", fmt]
        elif mode == "audio":
            cmd += ["--extract-audio", "--audio-format", fmt]

        print("\n[yt-dlp command]:", " ".join(cmd), "\n")

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        prog_re = re.compile(r"\[download\]\s+(\d{1,3}(?:\.\d)?)%")

        for ln in proc.stdout:
            if m := prog_re.search(ln):
                try:
                    pb["value"] = float(m.group(1))
                except ValueError:
                    pass
            log.insert("end", ln)
            log.see("end")

        proc.wait()
        pb["value"] = 100
        log.insert("end", f"\n{self.t('done')}\n")
        log.see("end")


if __name__ == "__main__":
    DownloaderGUI()
