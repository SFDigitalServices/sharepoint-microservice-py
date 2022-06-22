""" sharepoint module"""
#pylint: disable=too-few-public-methods,no-self-use
import json
import falcon
import jsend
import requests
from tasks import upload_file
from .hooks import validate_access

@falcon.before(validate_access)
class File():
    """Sharepoint File class"""
    def on_put(self, _req, resp, site_name):
        """
            upload a file to sharepoint drive
        """
        try:
            json_params = json.loads(_req.bounded_stream.read())

            if 'source_url' not in json_params:
                raise ValueError("Missing file source_url parameter")

            # check that something exists at the source_url
            response = requests.head(json_params['source_url'])
            response.raise_for_status()

            if 'destination_path' not in json_params:
                raise ValueError("Missing destination_path parameter")

            upload_file.apply_async(
                args=(
                    site_name,
                    json_params["source_url"],
                    json_params["destination_path"],),
                serializer='pickle'
            )

            resp.text = json.dumps(jsend.success({"msg": "success"}))
            resp.status = falcon.HTTP_200
        except Exception as err:    # pylint: disable=broad-except
            print("sharepoint.file on_put error:")
            print(f"{err}")
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))
