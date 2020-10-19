# https://www.hackerrank.com/challenges/magic-square-forming/problem

import math
import copy
import os
import random
import re
import sys

magic = [[2,7,6],[9,5,1],[4,3,8]]

def flip(s):
    return [s[2],s[1],s[0]]

def rotate(s):
    r=[[0,0,0],[0,0,0],[0,0,0]]

    r[0][0]=s[0][2]
    r[0][1]=s[1][2]
    r[0][2]=s[2][2]

    r[1][0]=s[0][1]
    r[1][1]=s[1][1]
    r[1][2]=s[2][1]
    
    r[2][0]=s[0][0]
    r[2][1]=s[1][0]
    r[2][2]=s[2][0]

    return r
def calculate_cost(s):
    cost=0
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - magic[i][j])
    return cost

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    cost = 99
    for i in range(8):
        if(i==4):
            s=flip(s)
        new_cost = calculate_cost(s)
        cost = new_cost if(new_cost<cost) else cost
        s = rotate(s)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
