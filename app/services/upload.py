from app.errors import FileExtNotAllowed
from app.core.config import Config
import os

ALLOWED_FILE_EXTENSIONS = ["torrent"]


def verify_file_extension(filename):
    extension = filename.split(".")[-1]
    if extension not in ALLOWED_FILE_EXTENSIONS:
        raise FileExtNotAllowed(extension)


def save_file(filename, file_raw):
    torrent_path = os.path.join(Config.TORRENT_UPLOAD_PATH, filename)
    with open(torrent_path, 'wb') as file:
        file.write(file_raw)
