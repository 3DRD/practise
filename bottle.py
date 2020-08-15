# Greedy algorithm


def fill(arr, m):
    arr.sort()
    count = 0
    for i in range(N):
        if m >= arr[i]:
            m -= arr[i]
            count += 1
        else:
            break
    return count


T = int(input())
N, X = map(int, input().split(" "))
result = []
for x in range(T):
    input1 = list(map(int, input().split(" ")))
    result.append(fill(input1, X))

print('\n'.join(map(str, result)))
