""" common functions for interacting with ms graph """
# pylint: disable=too-many-locals
import os
import requests
import msal

HOST_NAME = os.environ.get("SHAREPOINT_HOST_NAME")
CLIENT_ID = os.environ.get("SHAREPOINT_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SHAREPOINT_CLIENT_SECRET")
TENANT_ID = os.environ.get("SHAREPOINT_TENANT_ID")

AUTHORITY = "https://login.microsoftonline.com/" + TENANT_ID
ENDPOINT = "https://graph.microsoft.com/v1.0"

SCOPES = ['https://graph.microsoft.com/.default']

def get_access_token():
    """ get token from ms graph """
    app = msal.ConfidentialClientApplication(
            CLIENT_ID,
            authority=AUTHORITY,
            client_credential=CLIENT_SECRET)
    try:
        access_token = app.acquire_token_silent(SCOPES, account=None)
        if not access_token:
            try:
                access_token = app.acquire_token_for_client(scopes=SCOPES)
                print(f'accessToken: {access_token}')
                if access_token.get('access_token', False):
                    print('New access token retreived....')
                else:
                    print('Error aquiring authorization token. Check tenantID, clientID or clientSecret.') # pylint: disable=line-too-long
                    raise PermissionError("unable to acquire token")
            except Exception as err:
                raise err
        else:
            print('Token retreived from MSAL Cache....')

        return access_token['access_token']
    except Exception as err:
        print(f"get_access_token error: {err}")
        raise err

def make_request(method, resource, access_token, json_body=None):
    """ make a sharepoint request """
    results = requests.request(
        method,
        f'{ENDPOINT}{resource}',
        headers={
            'Authorization': f'Bearer {access_token}'},
        json=json_body)
    content = results.json() if results.content else {}
    print(f"make_request - {resource}: {content}")
    results.raise_for_status()
    return content

def get_site_id(site_name, access_token):
    """ retrieves site_id of given site_name """
    result = make_request('GET', f'/sites/{HOST_NAME}:/sites/{site_name}', access_token)
    return result['id']
