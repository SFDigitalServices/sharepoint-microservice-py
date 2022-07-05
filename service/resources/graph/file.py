""" file/drive related graph functions """
import os
from urllib.parse import urlparse
from io import BytesIO
import shutil
import tempfile
import requests
from service.resources.graph import common

# pylint: disable=too-many-locals

# must be multiple of 327,680 bytes
FILE_CHUNK_SIZE = int(os.environ.get("FILE_CHUNK_SIZE", "10485760"))

def get_default_drive_id(site_id, access_token):
    """ retrieves default drive id of given site_name """
    result = common.make_request('GET',f'/sites/{site_id}/drive', access_token)
    return result['id']

def list_drive_items(drive_id, access_token):
    """ list root items in drive """
    items = common.make_request('GET', f'/drives/{drive_id}/root/children', access_token)
    return {"items": items['value']}

def list_folder_items(drive_id, path_from_root, access_token):
    """ list items in folder """
    items = common.make_request(
        'GET',
        f'/drives/{drive_id}/root:/{path_from_root}:/children',
        access_token)
    return {"items": items['value']}

def get_item_info(site_id, path_from_root, access_token):
    """ retrieve file/folder meta data """
    item = common.make_request(
        'GET',
        f'/sites/{site_id}/drive/root:/{path_from_root}', access_token)
    return item


def upload_file(drive_id, file_url, upload_path_name, access_token):
    """ upload file found at file_url """
    upload_session = common.make_request(
        'POST',
        f'/drives/{drive_id}/items/root:/{upload_path_name}:/createUploadSession',
        access_token,
        json_body={
            '@microsoft.graph.conflictBehavior': 'rename'})
    upload_url = upload_session['uploadUrl']

    # retrieve the file
    parsed_file_url = urlparse(file_url)
    cloudstorage_domain = os.environ.get('CLOUDSTORAGE_DOMAIN')
    if cloudstorage_domain in parsed_file_url.netloc:
        # retrieve file through cloudstorage microservice
        cloudstorage_url = os.environ.get('CLOUDSTORAGE_URL')
        cloudstorage_api_key = os.environ.get('CLOUDSTORAGE_API_KEY')

        file_response = requests.get(
            cloudstorage_url,
            params={
                'name': parsed_file_url.path[1:],
                'apikey': cloudstorage_api_key
            },
            stream=True
        )
    else:
        # get file directly
        file_response = requests.get(file_url, stream=True)

    file_response.raise_for_status()

    # write file locally
    filename = os.path.basename(parsed_file_url.path)
    tmp_dir = tempfile.mkdtemp()
    local_file_path = os.path.join(tmp_dir, filename)
    with open(local_file_path, 'wb') as downloaded_file:
        shutil.copyfileobj(BytesIO(file_response.content), downloaded_file)
        del file_response

    # upload the file in chunks
    file_info = os.stat(local_file_path)
    file_size = file_info.st_size
    num_chunks = int(file_size/FILE_CHUNK_SIZE) + 1 if file_size % FILE_CHUNK_SIZE > 0 else 0
    with open(local_file_path, 'rb') as local_file:
        start = 0
        for this_chunk in range(num_chunks): # pylint: disable=unused-variable
            chunk = local_file.read(FILE_CHUNK_SIZE)
            content_length = len(chunk)
            chunk_range = f'bytes {start}-{start + content_length - 1}/{file_size}'
            upload_response = requests.request(
                'PUT',
                upload_url,
                headers={
                    'Content-Length': str(content_length),
                    'Content-Range': chunk_range
                },
                data=chunk
            )
            upload_response.raise_for_status()
            print(f"upload_response: - {upload_response.json()}")
            start += content_length
