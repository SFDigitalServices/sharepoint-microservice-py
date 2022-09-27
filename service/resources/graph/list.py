""" list related graph integrations """
from service.resources.graph import common

def get_site_lists(site_id, access_token):
    """ get lists in a site """
    lists = common.make_request('GET', f'/sites/{site_id}/lists', access_token)
    return {"lists": lists['value']}

def create_site_list(site_id, list_json, access_token):
    """ create a site list """
    if not "list" in list_json:
        list_json["list"] = {
            "template": "genericList"
        }

    resp = common.make_request(
        'POST',
        f'/sites/{site_id}/lists',
        access_token,
        json_body=list_json)
    return resp

def get_list_items(site_id, list_identifier, access_token):
    """ get items in a list """
    items = common.make_request(
        'GET',
        f'/sites/{site_id}/lists/{list_identifier}/items?expand=fields',
        access_token)
    return {"items": items['value']}

def get_list_item(site_id, list_identifier, item_id, access_token):
    """ get a single item in a list """
    item = common.make_request(
        'GET',
        f'/sites/{site_id}/lists/{list_identifier}/items/{item_id}',
        access_token)
    return item['fields']

def get_list_columns(site_id, list_identifier, access_token):
    """ get column definitions of a list """
    cols = common.make_request(
        'GET',
        f'/sites/{site_id}/lists/{list_identifier}/columns',
        access_token)
    return {"columns": cols['value']}

def add_list_item(site_id, list_identifier, item_json, access_token):
    """ add item to a list """
    item_json = {
        "fields": item_json
    }
    resp = common.make_request(
        'POST',
        f'/sites/{site_id}/lists/{list_identifier}/items',
        access_token,
        json_body=item_json)
    return resp

def update_list_item(site_id, list_identifier, item_id, item_json, access_token):
    """ update an item """
    resp = common.make_request(
        'PATCH',
        f'/sites/{site_id}/lists/{list_identifier}/items/{item_id}/fields',
        access_token,
        json_body=item_json
    )
    return resp

def delete_list_item(site_id, list_identifier, item_id, access_token):
    """ remove an item from a list """
    common.make_request(
        'DELETE',
        f'/sites/{site_id}/lists/{list_identifier}/items/{item_id}',
        access_token
    )
