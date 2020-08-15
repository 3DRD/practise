def isHappyNumber(num):
    rem ,sum = 0  ,0
    while (num > 0):
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum

def ishappy(result):
    while (result != 1 and result != 4):
        result = isHappyNumber(result)
    if result == 1:
        return 1
    elif result == 4:
        return 0


def isprime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return 0
    return 1


x, y, z = [int(n) for n in input().split(" ")]
count = 0
for i in range(x, y + 1):
    if ishappy(i) == 1 and isprime(i) == 1:
        count += 1
        print(i)

    if count == z:
        print(i)
        break

if z > count:
    print("Invalid index")




