"""Stdlib HUD + JSON API. Zero runtime deps."""

from __future__ import annotations

import argparse
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .state import World

HOST = "127.0.0.1"
PORT = 8765
ROOT = Path(__file__).resolve().parent.parent
HUD = ROOT / "hud"

_LOCK = threading.Lock()
_WORLD = World.seed()

_STATIC = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/hud.css": ("hud.css", "text/css; charset=utf-8"),
    "/hud.js": ("hud.js", "application/javascript; charset=utf-8"),
}


def _snapshot() -> dict[str, Any]:
    return _WORLD.snapshot()


def _read_json(handler: BaseHTTPRequestHandler) -> dict[str, Any]:
    length = int(handler.headers.get("Content-Length") or 0)
    if length <= 0:
        return {}
    raw = handler.rfile.read(length)
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


class Handler(BaseHTTPRequestHandler):
    server_version = "arena/0.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, name: str, mime: str) -> None:
        path = HUD / name
        if not path.is_file():
            self._send_json({"reject": "not_found"}, 404)
            return
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/state":
            with _LOCK:
                self._send_json(_snapshot())
            return
        static = _STATIC.get(path)
        if static:
            self._send_file(*static)
            return
        self._send_json({"reject": "not_found"}, 404)

    def do_POST(self) -> None:  # noqa: N802
        global _WORLD
        path = urlparse(self.path).path
        body = _read_json(self)
        with _LOCK:
            if path == "/tick":
                _WORLD = _WORLD.tick_step()
                self._send_json(_snapshot())
                return
            if path == "/hold":
                _WORLD = _WORLD.hold()
                self._send_json(_snapshot())
                return
            if path == "/correct":
                _WORLD = _WORLD.correct()
                self._send_json(_snapshot())
                return
            if path == "/reset":
                _WORLD = _WORLD.reset()
                self._send_json(_snapshot())
                return
            if path == "/inject":
                key = body.get("scenario")
                if not isinstance(key, str) or not key:
                    self._send_json({**_snapshot(), "reject": "unknown_scenario"}, 400)
                    return
                before = _WORLD
                _WORLD = _WORLD.inject(key)
                if _WORLD.reject == "unknown_scenario":
                    _WORLD = replace_reject(before, "unknown_scenario")
                    self._send_json(_snapshot(), 400)
                    return
                self._send_json(_snapshot())
                return
        self._send_json({"reject": "not_found"}, 404)


def replace_reject(world: World, reason: str) -> World:
    from dataclasses import replace

    return replace(world, reject=reason)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="arena", add_help=True)
    parser.add_argument("--host", default=HOST)
    parser.add_argument("--port", type=int, default=PORT)
    args = parser.parse_args(argv)
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"arena hud  http://{args.host}:{args.port}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstop", flush=True)
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
