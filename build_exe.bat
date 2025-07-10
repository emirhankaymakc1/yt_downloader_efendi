@echo off
cd /d %~dp0
echo [INFO] .exe oluşturuluyor...

"C:\Users\emirh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" ^
--noconfirm --onefile --windowed ^
--icon=icon.ico ^
--add-data "yt-dlp.exe;." ^
--add-data "ffmpeg\ffmpeg.exe;ffmpeg" ^
yt_gui_downloader.py

echo [BİTTİ] Oluşturuldu: dist\yt_gui_downloader.exe
pause
