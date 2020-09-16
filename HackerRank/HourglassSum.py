#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
#This could be done via BFS from each of the nonzero coordinates
#There is most likely an easier way however
#Can check the hourglass shape for all verticies, determine safety,
#Check if all non-zero, then keep track of the max
def hourglassSum(arr):
    max_sum = float("-inf") #Need to initialize to a small num since all squares migh be negative
    def is_safe(coord): #Array is always 6x6
        x,y = coord
        return x >= 0 and x < 6 and y >= 0 and y < 6

    def get_hourglass(x,y): #I accidentally reversed the rows,cols!
        up,down = (x-1,y),(x+1,y)
        left_up,right_up = (x-1,y-1),(x-1,y+1)
        left_down,right_down = (x+1,y-1),(x+1,y+1)

        res = [up,down,left_down,left_up,right_down,right_up]
        print(res)
        for move in res:
            if not is_safe(move):
                return []
        return res

    def get_hourglass_sum(hour):
        total = 0
        for elem in hour:
            total += arr[elem[0]][elem[1]]
        return total
        
    for i in range(6):
        for j in range(6):
            hourglass = get_hourglass(i,j)
            if hourglass != []:
                h_sum = get_hourglass_sum(hourglass) + arr[i][j]
                print(h_sum)
                max_sum = max(h_sum,max_sum)
    
    return max_sum #O(1) since the board size is constant


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()