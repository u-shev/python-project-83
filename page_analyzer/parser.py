from urllib.parse import urlparse


def parse_url(url):
    if url:
        o = urlparse(url)
        parsed_url = "{}://{}".format(o.scheme, o.netloc)
    else:
        parsed_url = ''
    return parsed_url
