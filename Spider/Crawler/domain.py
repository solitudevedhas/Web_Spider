from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# get first element in  url path
def get_first_elm_path(url):
    try:
        path = get_url_path(url).split("/")
        return path[1]
    except:
        return ''


# Get path in url after Domain (domain/<path>/)
def get_url_path(url):
    try:
        return urlparse(url).path
    except:
        return ''

# Get List of elements in Path
def get_elm_path(url):
    try:
        path = get_url_path(url).split("/")
        return path[1:-1]
    except:
        return ''