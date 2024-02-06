import numpy as np
import math
import random

from typing import Optional, Dict, List, Callable, Union


def divide(
    x:Union[int,float], 
    y:Union[int,float], 
    round:Optional[int]=None
):
    if y == 0:
        raise ValueError("y cannot be 0")
    
    if round:
        return round(x/y, round)
    else:
        return x/y

if __name__ = "__main__":

    X = 18
    Y = 3.5
    ROUND = 3
    divide(x=X, y=Y, round=ROUND)
    
