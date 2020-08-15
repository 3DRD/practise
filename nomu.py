import math

fact = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200,
        1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]


def minus(n1, n2):
    num = n1[0] * n2[1] - n1[1] * n2[0]
    den = n2[1] * n2[1]
    ans_num = num // math.gcd(num, den)
    ans_den = den // math.gcd(num, den)
    return [ans_num, ans_den]


def add(n1, n2):
    num = n1[0] * n2[1] + n1[1] * n2[0]
    den = n2[1] * n2[1]
    ans_num = num // math.gcd(num, den)
    ans_den = den // math.gcd(num, den)
    return [ans_num, ans_den]


def mul(n1, n2):
    num = n1[0] * n2[0]
    den = n1[1] * n2[1]
    ans_num = num // math.gcd(num, den)
    ans_den = den // math.gcd(num, den)
    return [ans_num, ans_den]


def exp(num, x):
    numerator = num[0] ** x
    denominator = num[1] ** x
    ans_num = numerator // math.gcd(numerator, denominator)
    ans_den = denominator // math.gcd(numerator, denominator)
    return [ans_num, ans_den]


def ncr(n, r):
    num = math.factorial(n)
    den = math.factorial(n-r) * math.factorial(r)
    ans_num = num // math.gcd(num, den)
    ans_den = den // math.gcd(num, den)
    return [ans_num, ans_den]


T = int(input())
for i in range(T):
    A, H, L1, L2, M, C = list(map(int, input().split(" ")))

    if (H - (A + C) * M) > 0:
        print("RIP")
        continue

    if (H - A * M) == 0:
        p1, p2 = 1, 1
        print(f'{p1}/{p2}')
        continue

    remain_H = H - (A * M)
    hits_required = math.ceil(remain_H / C)
    current_frac = [0, 1]
    prob_lucky = [L1 // math.gcd(L1, L2), L2 // math.gcd(L1, L2)]
    prob_unlucky = minus([1, 1], prob_lucky)

    for hit in range(hits_required, M + 1):
        current_prob = mul(exp(prob_lucky, hit), ncr(M, hit))
        current_not_prob = exp(prob_unlucky, M - hit)
        current_prob = mul(current_prob, current_not_prob)
        current_frac = add(current_frac, current_prob)

    print(f'{current_frac[0]}/{current_frac[1]}')
