#!/usr/bin/env python3
"""12. Type Checking"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type Checking At Last"""
    zoomed_in: List = [
        item * factor for item in lst
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
