from .decorators import sandbox
from .patcher import block_socket_access
from .socket import InternetAccessBlockedException

__version__ = '{major}.{minor}.{patch}'.format(major=1, minor=1, patch=0)
