""" sharepoint module"""
#pylint: disable=too-few-public-methods,no-self-use,broad-except,too-many-arguments
import json
import traceback
import falcon
import jsend
import requests
from tasks import upload_file
from service.resources.graph import common, list as sharepoint_list
from .hooks import validate_access

@falcon.before(validate_access)
class File():
    """Sharepoint File class"""
    def on_put(self, _req, resp, site_name):
        """
            upload a file to sharepoint drive
        """
        try:
            print("File.on_put")
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

            resp.text = json.dumps(jsend.success())
            resp.status = falcon.HTTP_200
        except Exception as err:
            print("sharepoint.file on_put error:")
            print(f"{err}")
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))

@falcon.before(validate_access)
class ListItems():
    """ Handle sharepoint list item requests """
    def on_post(self, _req, resp, site_name, list_identifier):
        """
            add item to a list
        """
        try:
            print("ListItems.on_post")
            json_params = json.loads(_req.bounded_stream.read())

            access_token = common.get_access_token()
            site_id = common.get_site_id(site_name, access_token)
            add_item_resp = sharepoint_list.add_list_item(
                site_id,
                list_identifier,
                json_params,
                access_token
            )

            resp.text = json.dumps(jsend.success(add_item_resp))
            resp.status = falcon.HTTP_200
        except Exception as err:
            print("sharepoint.ListItems on_post error:")
            print(f"{err}")
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))

@falcon.before(validate_access)
class SubsiteList():
    """ Handle sharepoint subsite list requests """
    def on_post(self, _req, resp, site_name, subsite_name, list_identifier):
        """
            add item to a subsite's list
        """
        try:
            print("SubsiteList.on_post")
            json_params = json.loads(_req.bounded_stream.read())

            access_token = common.get_access_token()
            subsite_id = common.get_subsite_id(site_name, subsite_name, access_token)
            add_item_resp = sharepoint_list.add_list_item(
                subsite_id,
                list_identifier,
                json_params,
                access_token
            )

            resp.text = json.dumps(jsend.success(add_item_resp))
            resp.status = falcon.HTTP_200
        except Exception as err:
            print("sharepoint.SubsiteList on_post error:")
            print(f"{err}")
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))

@falcon.before(validate_access)
class SubsiteListItem():
    """ Handle sharepont subsite list item requests """
    def on_get(self, _req, resp, site_name, subsite_name, list_identifier, item_id):
        """
            retrieve a subsite list item
        """
        try:
            print("SubsiteListItem.on_get")

            access_token = common.get_access_token()
            subsite_id = common.get_subsite_id(site_name, subsite_name, access_token)
            item = sharepoint_list.get_list_item(subsite_id, list_identifier, item_id, access_token)

            resp.text = json.dumps(jsend.success(item))
            resp.status = falcon.HTTP_200

        except Exception as err:
            print("sharepoint.SubsiteListItem on_get error:")
            print(f"{err}")
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))

    def on_patch(self, _req, resp, site_name, subsite_name, list_identifier, item_id):
        """
            update a subsite list item
        """
        try:
            print("SubsiteListItem.on_patch")

            json_params = json.loads(_req.bounded_stream.read())
            access_token = common.get_access_token()
            subsite_id = common.get_subsite_id(site_name, subsite_name, access_token)
            item = sharepoint_list.update_list_item(
                subsite_id,
                list_identifier,
                item_id,
                json_params,
                access_token)

            resp.text = json.dumps(jsend.success(item))
            resp.status = falcon.HTTP_200

        except Exception as err:
            print("sharepoint.SubsiteListIem on_patch error:")
            print(f"{err}")
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.text = json.dumps(jsend.error(f"{err}"))
