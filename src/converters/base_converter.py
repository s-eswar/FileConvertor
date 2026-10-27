from abc import ABC, abstractmethod

class BaseConverter(ABC):
    @abstractmethod
    def convert(self, *args, **kwargs):
        """Abstract method to be implemented by all converters."""
        pass