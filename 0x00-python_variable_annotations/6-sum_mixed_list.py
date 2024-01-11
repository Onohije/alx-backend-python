#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return a sum of all elements in mxd_lst"""
    from functools import reduce
    return reduce(lambda x, y: x + y, mxd_lst)
