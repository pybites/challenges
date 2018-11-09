import logging

from .__about__ import (
    __author__,
    __author_email__,
    __description__,
    __title__,
    __url__,
    __version__,
)
from .exceptions import DatabaseError
from . import (
    server,
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
