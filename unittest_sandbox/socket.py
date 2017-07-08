import socket


class InternetAccessBlockedException(Exception):
    pass


class SandboxSocket(socket.socket):
    """ Block the Socket module from accessing the internet """

    def __init__(self, *args, **kwargs):
        raise InternetAccessBlockedException('Internet access has been blocked by the @sandbox decorator!')
