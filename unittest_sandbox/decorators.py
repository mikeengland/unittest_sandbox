from unittest_sandbox.socket import SandboxSocket


def sandbox(func):
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
