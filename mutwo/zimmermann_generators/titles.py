import datetime
import typing

from mutwo import zimmermann_generators

__all__ = (
    "golden_number",
    "get_title",
)


def golden_number(date_time: typing.Optional[datetime.datetime] = None) -> int:
    """Get index in `metonic cycle <https://en.wikipedia.org/wiki/Metonic_cycle>`_.

    :param date_time: The current time. If set to ``None`` it will use current time.
    :type date_time: typing.Optional[datetime.datetime]
    :return: Number between 1 to 19. This is the current index of the metonic cycle.

    See `here <https://en.wikipedia.org/wiki/Golden_number_(time)>`_ for more
    information regarding golden numbers.
    """

    if date_time is None:
        date_time = datetime.datetime.now()

    year = date_time.year
    return (year % 19) + 1


def get_title(date_time: typing.Optional[datetime.datetime] = None) -> str:
    """Find title of current composition"""

    current_golden_number = golden_number(date_time)
    composition_counter = (
        zimmermann_generators.constants.GOLDEN_NUMBER_TO_COMPOSITION_COUNTER_DICT[
            current_golden_number
        ]
    ) + 1
    return f"{current_golden_number}.{composition_counter}"
