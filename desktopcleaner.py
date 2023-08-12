import os
import re
from datetime import date
import config
import dbox_oauth

dirs = config.directories()


# def file_move(directory=None, item=None):
# to_dir = dirs["to_dir"]
# new_dir = os.path.join(to_dir, mod_date)
# new_filepath = os.path.join(directory, item)

# if os.path.exists(directory):
#    filepath_retval = new_filepath
#    return (directory, filepath_retval)
# else:
#    os.mkdir(directory)
# filepath_retval = new_filepath
# return filepath_retval


def move_process(from_dir=None, upload_date=None):
    results = []
    to_dir = dirs["to_dir"]
    new_dir = os.path.join(to_dir, upload_date)
    for item in os.listdir(from_dir):
        filepath = os.path.join(from_dir, item)
        hidden = re.findall("^[.]", item)
        disk_image = re.findall(".dmg$", item)
        if hidden or disk_image:
            continue
        elif not os.path.isfile(filepath):
            continue
        else:
            new_filepath = os.path.join(new_dir, item)
            os.rename(filepath, new_filepath)
            results.append(item)
    retval = (new_dir, results)
    return retval


def dir_search():
    results = {}
    from_dirs = dirs["from_dirs"]
    run_date = date.today()
    run_date_string = run_date.strftime("%Y_%\d_%m")
    for from_dir in from_dirs:
        directory, moved_item = move_process(
            from_dir=from_dir, upload_date=run_date_string)
        results[from_dir] = moved_item

    print(f'files moved from: {results}')
    return directory


def main():
    try:
        access_token = dbox_oauth.oauth_flow()
        filepath = dir_search()
        dbox_oauth.to_dropbox(filepath=filepath, access_token=access_token)
    except Exception:
        quit()


if __name__ == "__main__":
    main()
