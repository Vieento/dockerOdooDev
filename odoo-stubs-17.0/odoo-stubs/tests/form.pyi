import collections
from typing import Any, Generic, Iterable, Iterator, TypeVar

from ..models import BaseModel

_ModelT = TypeVar("_ModelT", bound=BaseModel)
_FormT = TypeVar("_FormT", bound=Form)

MODIFIER_ALIASES: dict

class Form(Generic[_ModelT]):
    def __init__(self, record: _ModelT, view: Any | None = ...) -> None: ...
    def __getattr__(self, field_name: str): ...
    def __getitem__(self, field_name: str): ...
    def __setattr__(self, field_name: str, value) -> None: ...
    def __setitem__(self, field_name: str, value): ...
    def __enter__(self: _FormT) -> _FormT: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def save(self) -> _ModelT: ...
    @property
    def record(self) -> _ModelT: ...

class O2MForm(Form):
    def __init__(self, proxy: O2MProxy, index: int | None = ...) -> None: ...
    def save(self) -> None: ...

class UpdateDict(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def changed_items(self) -> Iterator[tuple]: ...
    def update(self, *args, **kw) -> None: ...
    def clear(self) -> None: ...

class X2MValue(collections.abc.Sequence):
    def __init__(self, iterable_of_vals: Iterable = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __contains__(self, id_) -> bool: ...
    def __getitem__(self, index): ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def get_vals(self, id_): ...
    def add(self, id_, vals) -> None: ...
    def remove(self, id_) -> None: ...
    def clear(self) -> None: ...
    def create(self, vals) -> None: ...
    def update(self, id_, changes, changed=...) -> None: ...
    def to_list_of_vals(self) -> list: ...

class O2MValue(X2MValue):
    def __init__(self, iterable_of_vals: Iterable = ...) -> None: ...
    def to_commands(self, convert_values=...) -> list: ...

class M2MValue(X2MValue):
    def to_commands(self) -> list: ...

class X2MProxy:
    def __init__(self, form: Form, field_name: str) -> None: ...
    @property
    def ids(self) -> list: ...

class O2MProxy(X2MProxy):
    def __len__(self) -> int: ...
    def new(self) -> O2MForm: ...
    def edit(self, index: int) -> O2MForm: ...
    def remove(self, index: int) -> None: ...

class M2MProxy(X2MProxy, collections.abc.Sequence):
    def __getitem__(self, index: int) -> BaseModel: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[BaseModel]: ...
    def __contains__(self, record: BaseModel) -> bool: ...
    def add(self, record: BaseModel) -> None: ...
    def remove(self, id: int | None = ..., index: int | None = ...) -> None: ...
    def set(self, records: BaseModel) -> None: ...
    def clear(self) -> None: ...

def convert_read_to_form(values: dict, fields: dict) -> dict: ...
def get_static_context(context_str: str) -> dict: ...

class Dotter:
    def __init__(self, values) -> None: ...
    def __getattr__(self, key): ...
