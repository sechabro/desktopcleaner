import os
from datetime import datetime
import config

desktop = config.desktop
documents = config.documents


def move_item(filepath=None, new_filepath=None):
    os.rename(filepath, new_filepath)
    return True


def date_mkdir(mod_date=None, item=None):
    new_dir = os.path.join(documents, mod_date)
    new_filepath = os.path.join(new_dir, item)
    if os.path.exists(new_dir):
        filepath_retval = (new_filepath)
        return filepath_retval
    else:
        os.mkdir(new_dir)
        print(f'{new_dir} created.')
        filepath_retval = (new_filepath)
        return filepath_retval


def main():
    results = []
    for item in os.listdir(desktop):
        filepath = os.path.join(desktop, item)
        metadata = os.stat((filepath))
        time = datetime.fromtimestamp(metadata.st_mtime)
        string_time = str(time)
        mod_date = string_time[0:10]
        new_filepath = date_mkdir(
            mod_date=mod_date, item=item)
        move_val = move_item(filepath=filepath, new_filepath=new_filepath)
        results.append(item)
    print(f'files moved: {results}')


if __name__ == "__main__":
    main()
