from unittest_sandbox import block_socket_access, InternetAccessBlockedException
from unittest import TestCase

from unittest_sandbox.tests.helpers import make_request

block_socket_access()


class PatcherTests(TestCase):
    def test_block_socket_access(self):
        with self.assertRaises(InternetAccessBlockedException):
            make_request('get')
