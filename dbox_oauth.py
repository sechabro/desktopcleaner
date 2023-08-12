import requests
import json
import config
from dropbox import DropboxOAuth2FlowNoRedirect
import dbox_selenium


def oauth_flow():
    creds = config.get_app_creds()
    auth_flow = DropboxOAuth2FlowNoRedirect(
        creds["key"], creds["secret"])
    auth_url = auth_flow.start()
    auth_code = dbox_selenium.get_auth_code(auth_url=auth_url)

    try:
        oauth_result = auth_flow.finish(auth_code)
        access_token = oauth_result.access_token
        print(access_token)
        return access_token
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def to_dropbox(filepath=None, access_token=None):
    url = "https://content.dropboxapi.com/2/files/upload"
    params = {"path": filepath,
              "mute": False,
              "mode": "add",
              "autorename": True,
              "strict_conflict": False
              }
    json_params = json.dumps(params)

    headers = {"Authorization": f'Bearer {access_token}',
               "Dropbox-API-Arg": f'{json_params}',
               "Content-Type": "application/octet-stream"
               }

    req = requests.request('POST', url, json=json_params, headers=headers)
    response = req.status_code
    return response


oauth_flow()
