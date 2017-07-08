from unittest import TestCase

import requests

from unittest_sandbox import (
    InternetAccessBlockedException,
    sandbox,
)

REQUESTS_METHODS = {
    'get': requests.get,
    'post': requests.post,
    'patch': requests.patch,
    'put': requests.put,
    'delete': requests.delete,
}


@sandbox
def make_request(method, *args, **kwargs):
    return REQUESTS_METHODS[method]('https://www.google.com', *args, **kwargs)


class SandboxDecoratorRequestsModuleTests(TestCase):
    def test_requests_get_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('get')

    def test_requests_post_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('post', data={})

    def test_requests_patch_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('patch', data={})

    def test_requests_put_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('put', data={})

    def test_requests_delete_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('delete', data={})
