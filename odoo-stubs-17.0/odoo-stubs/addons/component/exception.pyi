class ComponentException(Exception): ...
class NoComponentError(ComponentException): ...
class SeveralComponentError(ComponentException): ...
class RegistryNotReadyError(ComponentException): ...
