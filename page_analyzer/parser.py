from urllib.parse import urlparse


def parse_url(url):
    o = urlparse(url)
    parsed_url = "{}://{}".format(o.scheme, o.netloc)
    return parsed_url
