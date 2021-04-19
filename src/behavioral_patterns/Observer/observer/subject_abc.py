import abc
from observer.observer_abc import AbsObserver

class AbsSubject():
    __metaclass__ = abc.ABCMeta
    _observers = set()      # sucribers

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver class.')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        # clear set of observers - thus removing any dangling references
        self._observers.clear()