from abc import ABCMeta, abstractmethod

class AbsStrategy():
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""