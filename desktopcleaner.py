import os
import re
from datetime import date
import config
import dbox_oauth

dirs = config.directories()


def mkdir(upload_date=None):
    to_dir = dirs["to_dir"]
    new_dir = os.path.join(to_dir, upload_date)


def move_process(from_dir=None, new_subdir=None):
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
    return results


def dir_clean(directory=None):
    results = {}
    from_dirs = dirs["from_dirs"]
    for from_dir in from_dirs:
        moved_item = move_process(
            from_dir=from_dir, new_subdir=directory)
        results[from_dir] = moved_item

    print(f'files moved from: {results}')
    return


def main():
    run_date = date.today()
    run_date_string = run_date.strftime("%Y_%\d_%m")
    directory = mkdir(upload_date=run_date_string)
    try:
        access_token = dbox_oauth.oauth_flow()
        dir_clean(directory=directory)
        dbox_oauth.to_dropbox(filepath=directory, access_token=access_token)
    except Exception:
        quit()


if __name__ == "__main__":
    main()
