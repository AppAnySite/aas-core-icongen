from typing import Dict, Type

class ServiceLocator:
    _services: Dict[Type, object] = {}

    @classmethod
    def register(cls, interface: Type, implementation: object):
        cls._services[interface] = implementation

    @classmethod
    def resolve(cls, interface: Type):
        return cls._services.get(interface)
