from contextlib import AbstractContextManager
from typing import Any, Literal

PAIR: Literal[0]
PUB: Literal[1]
SUB: Literal[2]
REQ: Literal[3]
REP: Literal[4]
DEALER: Literal[5]
ROUTER: Literal[6]
PULL: Literal[7]
PUSH: Literal[8]

class Context:
    def __init__(self, io_threads: int = ...) -> None: ...
    def socket(
        self,
        socket_type: int,
    ) -> Socket: ...

class Socket(AbstractContextManager["Socket"]):
    def connect(self, addr: str) -> _SocketContext: ...
    def recv_string(
        self,
        flags: int | None = ...,
        encoding: str = ...,
    ) -> str: ...
    def send_string(
        self,
        u: str,
        flags: int | None = ...,
        copy: bool | None = ...,
        encoding: str = ...,
    ) -> None: ...
    def __exit__(self, *exc_info: Any) -> None: ...

class _SocketContext: ...
