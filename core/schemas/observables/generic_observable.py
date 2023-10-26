from typing import Literal

from core.schemas import observable


class GenericObservable(observable.Observable):
    """Use this type of Observable for any type of observable that doesn't fit into any other category."""
    type: Literal[observable.ObservableType.observable] = observable.ObservableType.observable


observable.TYPE_MAPPING[observable.ObservableType.observable] = GenericObservable
