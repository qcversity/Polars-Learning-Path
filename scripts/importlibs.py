import polars as pl
import pandas as pd
import time 
import os 
import sys
import numpy as np 
import pyarrow as pa 

print("*" * 42)
print("The imported libs are:".center(42))
print("*" * 42)

print(f"polars version is : {pl.__version__:>10}")
print(f"pandas version is : {pd.__version__:>10}")
print(f"numpy version is  : {np.__version__:>10}")
print(f"pyarrow version is: {pa.__version__:>10}")



print("*" * 42)