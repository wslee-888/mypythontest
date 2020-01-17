# -*- coding: utf-8 -*-
import socketserver
from typing import Iterable, Any


class MyTCPServer(socketserver.TCPServer,socketserver.ForkingMixIn):

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)

    def server_bind(self):
        super().server_bind()

    def server_activate(self):
        super().server_activate()

    def server_close(self):
        super().server_close()

    def fileno(self):
        return super().fileno()

    def get_request(self):
        return super().get_request()

    def shutdown_request(self, request):
        super().shutdown_request(request)

    def close_request(self, request):
        super().close_request(request)

    def serve_forever(self, poll_interval=0.5):
        super().serve_forever(poll_interval)

    def shutdown(self):
        super().shutdown()

    def service_actions(self):
        super().service_actions()

    def handle_request(self):
        super().handle_request()

    def _handle_request_noblock(self):
        super()._handle_request_noblock()

    def handle_timeout(self):
        super().handle_timeout()

    def verify_request(self, request, client_address):
        return super().verify_request(request, client_address)

    def process_request(self, request, client_address):
        super().process_request(request, client_address)

    def finish_request(self, request, client_address):
        super().finish_request(request, client_address)

    def handle_error(self, request, client_address):
        super().handle_error(request, client_address)

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def collect_children(self, *, blocking=False):
        super().collect_children(blocking=blocking)

    def __new__(cls) -> Any:
        return super().__new__(cls)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        return super().__ne__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    def __hash__(self) -> int:
        return super().__hash__()

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __delattr__(self, name: str) -> None:
        super().__delattr__(name)

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def __reduce__(self) -> tuple:
        return super().__reduce__()

    def __reduce_ex__(self, protocol: int) -> tuple:
        return super().__reduce_ex__(protocol)

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
