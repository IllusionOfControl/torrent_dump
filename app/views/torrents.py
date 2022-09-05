from flask import Blueprint, render_template, redirect, url_for, send_file, current_app, abort
from app.models import Torrent, File
import os


blueprint = Blueprint("torrents", __name__)


@blueprint.get("/")
@blueprint.get("/index")
def index():
    return redirect(url_for("torrents.retrieve_all_torrents"))


@blueprint.get("/torrents/")
@blueprint.get("/torrents/<int:page>")
def retrieve_all_torrents(page=1):
    torrents = Torrent.query.order_by(Torrent.id.desc()).paginate(page, 30, False)
    return render_template("torrents_list.html", torrents=torrents)


@blueprint.get("/torrent/<string:uid>")
def retrieve_torrent_info(uid):
    torrent = Torrent.query.filter_by(uid=uid).first_or_404()
    files = File.query.filter_by(torrent_id=torrent.id).all()
    return render_template("torrent_info.html", torrent=torrent, files=files)


@blueprint.get("/torrent/<string:uid>/delete")
def delete_torrent(uid):
    torrent = Torrent.query.filter_by(uid=uid).first_or_404()
    torrent.delete()
    return redirect(url_for("torrent.index"))


@blueprint.get("/torrent/<string:uid>/raw")
def retrieve_torrent_file(uid):
    torrent = Torrent.query.filter_by(uid=uid).first_or_404()
    file_path = os.path.join(current_app.config["TORRENT_UPLOAD_PATH"], uid)

    if os.path.isfile(file_path):
        return send_file(file_path, download_name=torrent.name + ".torrent")

    abort(404)
