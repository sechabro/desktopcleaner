import os


def directories():
    desktop = str(os.getenv('DTOP', default=None))
    documents = str(os.getenv('DOCS', default=None))
    downloads = str(os.getenv('DNLD', default=None))
    return [desktop, documents, downloads]
