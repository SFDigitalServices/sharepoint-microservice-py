""" celery tasks """

import celery
from kombu import serialization
import celeryconfig
from service.resources.graph import common
from service.resources.graph import file

# pylint: disable=unused-argument

serialization.register_pickle()
serialization.enable_insecure_serializers()

celery_app = celery.Celery('sharepoint-microservice')
celery_app.config_from_object(celeryconfig)

@celery_app.task(name="tasks.upload_file", bind=True)
def upload_file(self, site_name, source_url, destination_path):
    """
        upload a file to sharepoint drive
    """
    try:
        access_token = common.get_access_token()
        site_id = common.get_site_id(site_name, access_token)
        drive_id = file.get_default_drive_id(site_id, access_token)

        file.upload_file(drive_id, source_url, destination_path, access_token)
    except Exception as err: # pylint: disable=broad-except
        print("tasks.upload_file error:")
        print(f"{err}")
