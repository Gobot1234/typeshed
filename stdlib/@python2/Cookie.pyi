from typing import Any, Dict

class CookieError(Exception): ...

class Morsel(Dict[Any, Any]):
    key: Any
    def __init__(self): ...
    def __setitem__(self, K, V): ...
    def isReservedKey(self, K): ...
    value: Any
    coded_value: Any
    def set(self, key, val, coded_val, LegalChars=..., idmap=..., translate=...): ...
    def output(self, attrs: Any | None = ..., header=...): ...
    def js_output(self, attrs: Any | None = ...): ...
    def OutputString(self, attrs: Any | None = ...): ...

class BaseCookie(Dict[Any, Any]):
    def value_decode(self, val): ...
    def value_encode(self, val): ...
    def __init__(self, input: Any | None = ...): ...
    def __setitem__(self, key, value): ...
    def output(self, attrs: Any | None = ..., header=..., sep=...): ...
    def js_output(self, attrs: Any | None = ...): ...
    def load(self, rawdata): ...

class SimpleCookie(BaseCookie):
    def value_decode(self, val): ...
    def value_encode(self, val): ...

class SerialCookie(BaseCookie):
    def __init__(self, input: Any | None = ...): ...
    def value_decode(self, val): ...
    def value_encode(self, val): ...

class SmartCookie(BaseCookie):
    def __init__(self, input: Any | None = ...): ...
    def value_decode(self, val): ...
    def value_encode(self, val): ...

Cookie: Any
