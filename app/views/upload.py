from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.models import Torrent
from app.services.torrent import (
    generate_magnet,
    get_files_count,
    get_torrent_name,
    decode_metadata,
    calculate_download_size
)
from app.services.upload import verify_file_extension, save_file
import uuid
import hashlib


blueprint = Blueprint("upload", __name__)


@blueprint.route("/upload", methods=["GET"])
def retrieve_upload_form():
    return render_template("upload.html")


@blueprint.route('/upload', methods=["POST"])
def upload_file():
    if "torrents" not in request.files:
        flash('No file part')
        return redirect(url_for("retrieve_upload_form"))

    upload_files = request.files.getlist("torrents")

    for file in upload_files:
        try:
            verify_file_extension(file.filename)
            file_raw = file.read()
            metadata = decode_metadata(file_raw)
        except Exception as e:
            flash(str(e))
            break

        torrent_name = get_torrent_name(metadata)
        download_size = calculate_download_size(metadata)
        files_count = get_files_count(metadata)
        uid = uuid.uuid4().hex
        md5 = hashlib.md5(file_raw).hexdigest()
        magnet_link = generate_magnet(metadata)

        torrent = Torrent(
            uid=uid,
            name=torrent_name,
            download_size=download_size,
            files_count=files_count,
            md5_hash=md5,
            magnet_link=magnet_link
        )

        torrent.save()
        save_file(torrent.uid, file_raw)

    return redirect("/")
