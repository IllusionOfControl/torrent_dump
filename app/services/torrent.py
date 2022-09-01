from urllib import parse as url_parse
import bencode
import hashlib
import base64


def decode_metadata(raw_torrent):
    metadata = bencode.bdecode(raw_torrent)
    return metadata


def get_torrent_name(metadata):
    return metadata["info"]["name"]


def generate_magnet(metadata):
    magnet_uri = "magnet:?%s"

    info_field = bencode.bencode(metadata['info'])
    digest_hash = hashlib.sha1(info_field).digest()
    b32_hash = base64.b32encode(digest_hash)

    params = {
        "xt": "urn:btih:%s" % b32_hash,
        "dn": metadata["info"]["name"],
        "tr": metadata["announce"],
    }

    param_str = url_parse.urlencode(params)

    return magnet_uri % param_str


def check_single_file_download(metadata):
    return "files" not in metadata["info"]


def calculate_download_size(metadata):
    if check_single_file_download(metadata):
        return metadata["info"]["length"]
    else:
        files_size = [file["length"] for file in metadata["info"]["files"]]
        return sum(files_size)


def get_files_count(metadata):
    if check_single_file_download(metadata):
        return 1
    else:
        return len(metadata["info"]['files'])


def get_file_list(metadata):
    return metadata["info"]['files']
