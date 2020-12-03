# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:16:55 2020

Solution for project euler problem 10

@author: gguil
"""
import numpy as np
import os
import time
numberString = open(os.path.dirname(__file__)+"/data/problem10data.txt").read().split()
numberArray = np.array(numberString).reshape((20, 20))
subsets = set()

def read_down(i, j):
    array = numberArray[i:i+4, j:j+1]
    l = list()
    for x in array:
        l.append(x[0])
    t = tuple(l)
    subsets.add(t)


def read_right(i, j):
    m = map(tuple, numberArray[i:i+1, j:j+4])
    t = tuple(m)
    subsets.add(t[0])


def read_rd(i, j):
    l = [numberArray[i, j], numberArray[i+1, j+1],
         numberArray[i+2, j+2], numberArray[i+3, j+3]]
    t = tuple(l)
    subsets.add(t)


def read_ld(i, j):
    l = [numberArray[i, j], numberArray[i+1, j-1],
         numberArray[i+2, j-2], numberArray[i+3, j-3]]
    t = tuple(l)
    subsets.add(t)
    
def main():
    start = time.time()
    rows = 20
    cols = 20
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
    containsZeros = set()
    for t in subsets:
        if "00" in t:
            containsZeros.add(t)
    finalSet = subsets.difference(containsZeros)
    largestTuple = tuple()
    largestProduct = 0
    for t in finalSet:
        temp = 1
        for x in t:
            temp *= int(x)
        if temp == 0:
            print("you missed some zeros: " + str(t))
        if temp > largestProduct:
            largestProduct = temp
            largestTuple = t
    end = time.time()
    print("The largest product is: " + str(largestProduct) + " and it is the product of: " + str(largestTuple))
    print("Ran in: " + str(end - start) + " seconds")


if __name__ == "__main__":
    main()

