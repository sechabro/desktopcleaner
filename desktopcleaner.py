import os
import re
import requests
import json
from datetime import datetime
import config

dirs = config.directories()
auth_token = config.get_token()


def date_mkdir(mod_date=None, item=None):
    to_dir = dirs["to_dir"]
    new_dir = os.path.join(to_dir, mod_date)
    new_filepath = os.path.join(new_dir, item)

    if os.path.exists(new_dir):
        filepath_retval = new_filepath
        return filepath_retval
    else:
        os.mkdir(new_dir)
        filepath_retval = new_filepath
        return filepath_retval


def timestamp_format(time=None):
    string_time = str(time)
    mod_date = string_time[0:10]
    return mod_date


def move_process(from_dir=None):
    results = []
    for item in os.listdir(from_dir):
        filepath = os.path.join(from_dir, item)
        hidden = re.findall("^[.]", item)
        if hidden:
            continue
        elif not os.path.isfile(filepath):
            continue
        else:
            metadata = os.stat((filepath))
            time = datetime.fromtimestamp(metadata.st_mtime)
            mod_date = timestamp_format(time=time)
            new_filepath = date_mkdir(
                mod_date=mod_date, item=item)
            os.rename(filepath, new_filepath)
            results.append(item)
    return results


def to_dropbox(token=None, filepath=None, content_hash=None):
    url = "https://content.dropboxapi.com/2/files/upload"
    params = {"path": filepath,
              "mute": False,
              "mode": "add",
              "autorename": True,
              "strict_conflict": False
              }
    json_params = json.dumps(params)

    headers = {"Authorization": f'Bearer {token}',
               "Dropbox-API-Arg": f'{json_params}',
               "Content-Type": "application/octet-stream"
               }

    req = requests.request('POST', url, json=json_params, headers=headers)
    response = requests.Response.json(req)
    print(response)


def main():
    results = {}
    from_dirs = dirs["from_dirs"]

    for from_dir in from_dirs:
        moved_item = move_process(from_dir=from_dir)
        results[from_dir] = moved_item

    print(f'files moved from: {results}')


if __name__ == "__main__":
    main()
