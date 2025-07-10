
# YT Downloader | €fendi

📥 Tkinter tabanlı YouTube video/ses indirici arayüzü  
📥 Tkinter-based YouTube video/audio download GUI

---

## 🇹🇷 Özellikler (Türkçe)

- Tek video veya çalma listesi indirimi
- Ses veya video olarak indirme seçeneği
- Farklı çözünürlük ve formatlar (mp4, mp3, webm, m4a, mkv)
- Oturum bilgisiyle indirme (cookies.txt)
- Anlık dil değiştirme (TR, EN, FR, DE, ES, PT)
- Tema seçimi: Açık/Koyu
- EXE olarak paketlenebilir

### 💻 Kullanım

#### Python ile çalıştırmak için:
```bash
python yt_gui_downloader.py
```

#### EXE (Windows) olarak:
- `dist/yt_gui_downloader.exe` dosyasını çift tıkla.

### 🔧 Gerekli Bağımlılıklar

- Python 3.10+
- `yt-dlp.exe`
- `ffmpeg`
- `ttkbootstrap` (isteğe bağlı, arayüz temasını iyileştirir)

---

## 🇬🇧 Features (English)

- Download single videos or entire playlists
- Choose between audio or video download
- Supports multiple resolutions and formats (mp4, mp3, webm, m4a, mkv)
- Login-based download with cookies.txt
- Live language switch (TR, EN, FR, DE, ES, PT)
- Light/Dark theme support
- Can be packaged as a standalone EXE

### 💻 Usage

#### Run with Python:
```bash
python yt_gui_downloader.py
```

#### Run as EXE (Windows):
- Double click `dist/yt_gui_downloader.exe`

### 🔧 Dependencies

- Python 3.10+
- `yt-dlp.exe`
- `ffmpeg`
- `ttkbootstrap` (optional for themed GUI)

---

## 🛠 Derleme / Building (PyInstaller ile EXE yapmak)

```bash
pyinstaller --noconfirm --onefile --windowed --icon="icon.ico" ^
--add-data "ffmpeg;ffmpeg" ^
--add-data "yt-dlp.exe;." ^
yt_gui_downloader.py
```

---

## 📂 Klasör Yapısı / Folder Structure

```
yt_downloader_efendi/
├── yt_gui_downloader.py
├── yt-dlp.exe
├── ffmpeg/
├── icon.ico
├── README.md
└── dist/
    └── yt_gui_downloader.exe
```

---

## 📜 Lisans / License

MIT License
