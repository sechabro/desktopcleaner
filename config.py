import os


def directories():
    from_dir1 = str(os.getenv('DTOP', default=None))
    from_dir1 = str(os.getenv('DOCS', default=None))
    from_dir2 = str(os.getenv('DNLD', default=None))
    return [from_dir1, from_dir1, from_dir2]
