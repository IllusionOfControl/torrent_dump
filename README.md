# Torrent dump

Windows:
```sh
$env:FLASK_APP="app.main:app"; flask db upgrade
python run.py
```

Docker:
```sh
docker build -t torrent_dump .
docker run -it --name torrent_dump -v ${PWD}/data:/app/data -p 8000:8000 torrent_dump
```