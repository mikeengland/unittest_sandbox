import inspect

from unittest_sandbox.socket import SandboxSocket


def sandbox_decorator(func):
    """
    A decorator which raises an InternetAccessBlocked exception if the decorated unit test
    method tries to access the internet.

    :param func: The decorated function
    :return: A new function that blocks the socket module from accessing the internet
    """

    def wrapped(self, *args, **kwargs):
        import socket
        socket.socket = SandboxSocket
        return func(self, *args, **kwargs)

    return wrapped


def sandbox(*args, **kwargs):
    """
    Utility decorator to apply the sandbox_decorator decorator to all methods
    inside the class starting with 'test_', or a single decorated test method.
    Inspired by https://stackoverflow.com/a/6307868/1224372
    """

    def decorate(cls):
        if inspect.isfunction(cls):
            return sandbox_decorator(cls)

        for attr in dir(cls):
            if callable(getattr(cls, attr)) and attr.startswith('test_'):
                setattr(cls, attr, sandbox_decorator(getattr(cls, attr)))
        return cls

    return decorate
