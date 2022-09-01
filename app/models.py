from app.database import database as db
from sqlalchemy.sql import func
from typing import List, Type


class CRUDMixin:
    def update(self, commit: bool = True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save()

    def save(self, commit: bool = True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit: bool = True):
        db.session.delete(self)
        if commit:
            db.session.commit()
        return self

    @staticmethod
    def save_all(objects: List[Type[db.Model]]):
        db.session.add_all(objects)
        db.session.commit()


class Torrent(CRUDMixin, db.Model):
    __tablename__ = "torrents"

    uid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(256))
    download_size = db.Column(db.Integer)
    files_count = db.Column(db.Integer)
    md5_hash = db.Column(db.String(32))
    magnet_link = db.Column(db.String)
    uploaded_at = db.Column(db.DateTime, server_default=func.now())
    is_removed = db.Column(db.Boolean, default=False)


class File(CRUDMixin, db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(256))
    size = db.Column(db.Integer)
    