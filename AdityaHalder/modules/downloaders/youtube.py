from os import path
from yt_dlp import YoutubeDL
from AdityaHalder.modules.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
