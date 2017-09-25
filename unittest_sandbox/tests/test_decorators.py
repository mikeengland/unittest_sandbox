from unittest import TestCase

from unittest_sandbox import (
    InternetAccessBlockedException,
    sandbox,
)
from unittest_sandbox.tests.helpers import make_request


class FunctionLevelDecoratorTests(TestCase):
    @sandbox()
    def test_requests_get_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('get')

    @sandbox()
    def test_requests_post_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('post', data={})

    @sandbox()
    def test_requests_patch_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('patch', data={})

    @sandbox()
    def test_requests_put_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('put', data={})

    @sandbox()
    def test_requests_delete_method_raises_exception(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('delete', data={})


@sandbox()
class ClassLevelDecoratorTests(TestCase):
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
