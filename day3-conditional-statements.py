#!/bin/python3

import math
import os
import random
import re
import sys


def checkNum(N):
    if N%3==0:
        print('Weird')
    elif N%3!=0 and (N>=2 and N<=5):
        print('Not Weird')
    elif N%3!=0 and (N>=6 and N<=20):
        print('Weird')
    elif N%3!=0 and (N>20):
        print('Not Weird')
    else:
        print('Other')

N = int(input())
checkNum(N)


if __name__ == '__main__':
    N = int(input())
