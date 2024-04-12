from enum import IntEnum


class CirculationType(IntEnum):
    CHECKOUT = 1
    RETURN = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ReservationStatus(IntEnum):
    NOT_FULFILLED = 1
    CAN_BE_FULFILLED = 2
    FULFILLED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
