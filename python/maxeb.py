import pandas as pd
import numpy as np
import sys
import os
import csv
from remerkleable.basic import uint64
from remerkleable.basic import uint
from remerkleable.core import View
from hashlib import sha256
from remerkleable.byte_arrays import Bytes32
from typing import Union

current_wd = os.getcwd
print(current_wd)
current_path = sys.path
print(current_path)

# Checking the Gwei value that Mike had written down in a blog post (Can't remember which one!)

def integer_squareroot(n):
    """
    Return the largest integer ``x`` such that ``x**2 <= n``.
    """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

brf = 64
teb = 24 * 10**6 * 10**9 # 24 million in Gwei
sqrtteb = integer_squareroot(teb)
ebi = 10**9 # effective balance increment
br = ebi * brf // sqrtteb
print(br)
print(sqrtteb)
print(sqrtteb**2)

tebeth = 24 * 10**6
tebethsqrt = integer_squareroot(tebeth)
print(tebethsqrt)
print(tebethsqrt**2)

"""
    Check statements
"""
balance = 32
EFFECTIVE_BALANCE_INCREMENT = 1
MAX_EFFECTIVE_BALANCE = 32

validator_effective_balance = min(balance - balance % EFFECTIVE_BALANCE_INCREMENT, MAX_EFFECTIVE_BALANCE)

print(validator_effective_balance)
print(32%1)                            # % is modulo operator


## Simulate the random integers for proposer selection
## ====================================================
i = 0
#seed = bytes([10])

ZERO_BYTES32 = b'\x00' * 32

def hash(x: Union[bytes, bytearray, memoryview]) -> Bytes32:
    return Bytes32(sha256(x).digest())

def serialize(obj: View) -> bytes :
    return obj.encode_bytes()

def uint_to_bytes(n: uint) -> bytes:
    return serialize(n)

seed = hash(bytes([10]))  # set some seed value   
data = []

# Iterate until the validator set total is reached (716,800 in the blog post example scenario)
for i in range(1,716800):
    random_byte = hash(seed + uint_to_bytes(uint64(i // 32)))[i % 32]
    print(random_byte)
    data.append([i,random_byte])
#data

df = pd.DataFrame(data, columns = ['iteration','random byte'])
#df

# Write results to csv file for visualisation
# --------------------------------------------
df.to_csv('/Users/sandra/data/validator/validator_random_bytes.csv')
