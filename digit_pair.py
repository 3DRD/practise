# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:01:54 2020

@author: DRD PC
"""


def bit_score(n, digits):
    temp = 0
    for i in range(n):
        temp = max_digit(digits[i]) * 11 + min_digit(digits[i]) * 7
        if temp >= 100:
            temp %= 100
            digits[i] = int(temp)
        else:
            digits[i] = int(temp)
    return digits


def max_digit(digit):
    max = 0
    d = 0
    while (digit != 0):
        d = digit % 10
        if d >= max:
            max = d
        digit = int(digit / 10)
    return max


def min_digit(digit):
    min = 100
    d = 0
    while (digit != 0):
        d = digit % 10
        if d <= min:
            min = d
        digit = int(digit / 10)
    return min


def check_significant(a, b):
    if a / 10 == b / 10:
        return 1
    else:
        return 0


refer = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
N = int(input())
indices = input()
digits = indices.split(' ')
for i in range(N):
    digits[i] = int(digits[i])
bit_score(N, digits)
pair = 0
for i in range(N):
    temp_pair = 0
    for j in range(N):

        if i % 2 == 0 and j % 2 == 0:
            if check_significant(digits[i], digits[j]) == 1:
                check = int(digits[j] / 10)
                if refer[check][1] != 2 and int(digits[j]) != int(digits[i]):
                    refer[check][1] += 1
                    temp_pair += 1

        if i % 2 == 1 and j % 2 == 1:
            if check_significant(digits[i], digits[j]) == 1:
                check = int(digits[j] / 10)
                if refer[check][1] != 2 and int(digits[j]) != int(digits[i]):
                    refer[check][1] += 1
                    temp_pair += 1

    pair += temp_pair

print(pair)
