# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:09:00 2020

@author: DRD PC
"""


def most_bachelorette(N, bride, groom):
    count = 1
    for i in range(N):
        if bride[0] == groom[0]:
            count = 0
            break

        else:
            temp = groom[0]
            groom = groom[1:N]
            groom += temp

    if count == 0:
        return 0
    else:
        return 1


pair = 0
N = int(input(""))
bride = input("")
groom = input("")
t = N
n = most_bachelorette(N, bride, groom)
if n == 1:
    print(N)

else:
    for i in range(N):
        for j in range(N):

            if bride[0] == groom[0]:
                bride = bride[1:N]
                groom = groom[1:N]
                pair += 1
                N -= 1
                i = 0
                break
            elif j == N - 1:
                break
            else:
                temp = groom[0]
                groom = groom[1:N]
                groom += temp
    print(t - pair)
