import requests

REQUESTS_METHODS = {
    'get': requests.get,
    'post': requests.post,
    'patch': requests.patch,
    'put': requests.put,
    'delete': requests.delete,
}


def make_request(method, *args, **kwargs):
    return REQUESTS_METHODS[method]('https://www.google.com', *args, **kwargs)
