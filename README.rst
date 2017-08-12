unittest-sandbox
================

unittest-sandbox provides a @sandbox decorator which ensures unit test
methods do not make any socket/web requests during test execution. Note:
This currently only works with Python 3.

Installation
------------

To install run: ``pip install unittest_sandbox``

Example usage
-------------

.. code:: python

    from unittest import TestCase

    import requests

    from unittest_sandbox import InternetAccessBlockedException, sandbox

    # The @sandbox() decorator can be applied to methods individually like below

    class RequestTests(TestCase):
        def test_non_request_works(self):
            self.assertEqual(1 + 1, 2)

        @sandbox()
        def test_web_request_raises_exception_when_sandbox_decorator_is_applied(self):
            # If a web request is sent in a test method wrapped with the @sandbox decorator,
            # an InternetAccessBlockedException will be raised.

            with self.assertRaises(InternetAccessBlockedException):
                requests.get('https://www.google.com')

    # The @sandbox() decorator can also be applied to the class as a whole. This is the same as decorating
    # all 'test_' methods with @sandbox()

    @sandbox()
    class RequestTests(TestCase):
        def test_non_request_works(self):
            self.assertEqual(1 + 1, 2)

        def test_web_request_raises_exception_when_sandbox_decorator_is_applied(self):
            # If a web request is sent in a test method wrapped with the @sandbox decorator,
            # an InternetAccessBlockedException will be raised.

            with self.assertRaises(InternetAccessBlockedException):
                requests.get('https://www.google.com')

