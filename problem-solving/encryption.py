# https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s=''.join(s.split())
    root = math.sqrt(len(s))
    x = math.ceil(root)
    y = math.floor(root)
    y = y+1 if(x*y<len(s)) else y
    arr = [s[i*x:(i+1)*x] for i in range(y)]
    
    ret =''
    for i in range(x):
        for j in arr:
            try:
                ret+=j[i]
            except:
                pass
        ret+=' '


    return ret.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
