# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:16:55 2020

Solution for project euler problem 10

@author: gguil
"""
import numpy as np

numberString = open("data\problem10data.txt").read().split()
numberArray = np.array(numberString).reshape((20, 20))
subsets = set()

def read_down(i, j):
    m = map(tuple, numberArray[i:i+4, j:j+1])
    t = tuple(m)
    print(t)
    subsets.update(t)


def read_right(i, j):
    m = map(tuple, numberArray[i:i+1, j:j+4])
    t = tuple(m)
    subsets.update(t)


def read_rd(i, j):
    l = [numberArray[i, j], numberArray[i+1, j+1],
         numberArray[i+2, j+2], numberArray[i+3, j+3]]
    t = tuple(l)
    subsets.update(t)


def read_ld(i, j):
    l = [numberArray[i, j], numberArray[i+1, j-1],
         numberArray[i+2, j-2], numberArray[i+3, j-3]]
    t = tuple(l)
    subsets.update(t)
    
def main():
    rows = 5
    cols = 5
    for i in range(rows):
        for j in range(cols):
            if i <= 16:
                if j > 2 and j < 17:
                    read_down(i, j)
                    read_right(i, j)
                    read_rd(i, j)
                    read_ld(i, j)
                if j <= 2:
                    read_down(i, j)
                    read_right(i, j)
                    read_rd(i, j)
                if j > 16:
                    read_down(i, j)
                    read_ld(i, j)
            if i > 16:
                if j <= 16:
                    read_right(i, j)
                if j > 16:
                    continue
    print(subsets)
    filter(lambda s: '00' in s ,subsets)
    print("--------------------------------------------")
    print(subsets)

if __name__ == "__main__":
    main()

