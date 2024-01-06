import os 
import sys
import pathlib
from pathlib import Path
import time 
import re
import shutil

import numpy as np 
import pyarrow as pa 

import polars as pl
import pandas as pd


_builtin_modules = [
    'os',
    'sys',
    'pathlib',
    'time',
    'shutil',
    're'
]

print("*" * 42)
print("The imported libs are:".center(42))
print("*" * 42)

print(f"polars version is : {pl.__version__:>10}")
print(f"pandas version is : {pd.__version__:>10}")
print(f"numpy version is  : {np.__version__:>10}")
print(f"pyarrow version is: {pa.__version__:>10}")

print("*" * 42)
print("The imported builtin modules are:\n",_builtin_modules, sep="")

print("*" * 62)
print(f"The python executable path is:\n {sys.executable}")
print("*" * 62)


def typewriter_message(message, delay=0.01):
    """
    Prints a message to the screen, typewriter style.

    Args:
    - message (str): The message to be printed.
    - delay (float): The delay in seconds between each character.
    """
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  
    
print()

typewriter_message("."*20)
typewriter_message("Important Reminder:")
typewriter_message("."*20)

message = "\nBefore proceeding, please ensure that you have activated the appropriate virtual environment for this project.\nThis step is crucial to maintain consistent dependencies and project settings."

typewriter_message(message)
typewriter_message("."*79)