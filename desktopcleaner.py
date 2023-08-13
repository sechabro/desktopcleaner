import os
import re
from datetime import date
import config
import dbox_oauth
import time

dirs = config.directories()


def mkdir(upload_date=None):
    to_dir = dirs["to_dir"]
    new_dir = os.path.join(to_dir, upload_date)
    os.mkdir(new_dir)
    return new_dir


def move_process(from_dir=None, new_subdir=None, access_token=None):
    results = []
    for item in os.listdir(from_dir):
        filepath = os.path.join(from_dir, item)
        hidden = re.findall("^[.]", item)
        disk_image = re.findall(".dmg$", item)
        if hidden or disk_image:
            continue
        elif not os.path.isfile(filepath):
            continue
        else:
            new_filepath = os.path.join(new_subdir, item)
            os.rename(filepath, new_filepath)
            results.append(item)
            upload = dbox_oauth.to_dropbox(
                filepath=new_filepath, access_token=access_token)
            print(f'response {upload} for {item}')
    return results


def dir_clean(directory=None):
    results = {}
    access_token = dbox_oauth.oauth_flow()
    from_dirs = dirs["from_dirs"]
    for from_dir in from_dirs:
        moved_item = move_process(
            from_dir=from_dir, new_subdir=directory, access_token=access_token)
        results[from_dir] = moved_item

    print(f'files moved from: {results}')
    return


def main():
    run_date = date.today()
    run_date_string = run_date.strftime("%Y_%d_%m")
    directory = mkdir(upload_date=run_date_string)
    try:
        dir_clean(directory=directory)
    except Exception:
        quit()


if __name__ == "__main__":
    main()
