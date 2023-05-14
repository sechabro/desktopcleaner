import os


def directories():
    dirs = {}
    dirs["from_dirs"] = [str(os.getenv('DTOP', default=None)), str(
        os.getenv('DNLD', default=None))]
    dirs["to_dir"] = str(os.getenv('DOCS', default=None))

    return dirs
