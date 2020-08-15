"""

Consecutive Prime Sum

Problem Description

Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

    For example
        5 = 2 + 3,
        17 = 2 + 3 + 5 + 7,
        41 = 2 + 3 + 5 + 7 + 11 + 13.
        Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000

"""


def is_prime(N):
    count = 0
    for i in range(2, N + 1):
        if N % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def prime_sum(arr, N):
    sumlist = []
    count = 0

    for i in range(0, len(arr)):
        sumlist.append(sum(arr[0:i],0))

    for i in arr[1:]:
        if i in sumlist:
            count += 1

    return count


N = int(input())
arr = range(2, N + 1)
prime_array = list(filter(is_prime, arr))
result = prime_sum(prime_array,N)
print(result)

