#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    p = 0
    while ar:
        v = ar[0]
        try:
            # ar = []
            ar.pop(ar.index(v))
            ar.pop(ar.index(v))
            p += 1
        except (IndexError, ValueError):
            continue

    return p

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
