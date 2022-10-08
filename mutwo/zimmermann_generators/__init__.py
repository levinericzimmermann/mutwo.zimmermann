"""Generators used by Levin Zimmermann.

titles: Create the titles of compositions. After each
        composition a new major release of this package
        has to be done, to ensure to avoid duplication
        of titles.

"""

from . import constants

from .extended_chomsky import *
from .interlockings import *
from .titles import *

from mutwo import core_utilities

__all__ = core_utilities.get_all(extended_chomsky, interlockings, titles)

# Force flat structure
del core_utilities, extended_chomsky, interlockings, titles
