from .socket import SandboxSocket


def block_socket_access():
    import socket
    socket.socket = SandboxSocket
