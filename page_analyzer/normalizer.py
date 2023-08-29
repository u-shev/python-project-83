from urllib.parse import urlparse


def normalize_url(url):
    if url:
        o = urlparse(url)
        normalized_url = "{}://{}".format(o.scheme, o.netloc)
    else:
        normalized_url = ''
    return normalized_url
