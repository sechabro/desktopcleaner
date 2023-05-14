import os
from datetime import datetime
import config

dirs = config.directories()


def move_item(filepath=None, new_filepath=None):
    if os.path.isfile(filepath):
        os.rename(filepath, new_filepath)
        return True
    elif not os.path.isfile(filepath):
        return False


def date_mkdir(mod_date=None, item=None):
    to_dir = dirs["to_dir"]
    new_dir = os.path.join(to_dir, mod_date)
    new_filepath = os.path.join(new_dir, item)

    if os.path.exists(new_dir):
        filepath_retval = new_filepath
        return filepath_retval
    else:
        os.mkdir(new_dir)
        print(f'{new_dir} created.')
        filepath_retval = new_filepath
        return filepath_retval


def timestamp_format(time=None):
    string_time = str(time)
    mod_date = string_time[0:10]
    return mod_date


def main():
    results = []
    from_dirs = dirs["from_dirs"]

    for from_dir in from_dirs:

        for item in os.listdir(from_dir):
            filepath = os.path.join(from_dir, item)
            metadata = os.stat((filepath))
            time = datetime.fromtimestamp(metadata.st_mtime)
            mod_date = timestamp_format(time=time)
            new_filepath = date_mkdir(
                mod_date=mod_date, item=item)
            move_val = move_item(filepath=filepath, new_filepath=new_filepath)

            if move_val is False:
                continue
            else:
                results.append(item)

        print(f'files moved from {from_dir}: {results}')


if __name__ == "__main__":
    main()
