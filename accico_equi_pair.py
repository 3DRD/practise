N = int(input())
arr = list(map(int, input().split(" ")))


def check_equi(i, j):
    if sum(arr[0:i]) == sum(arr[i + 1:j]) == sum(arr[j + 1:]):
        return 1
    else:
        return 0


x = 0
for i in range(0, N - 1):
    for j in range(i + 1, N):
        x = check_equi(i, j)
        if x == 1:
            break
    if x == 1:
        break

if x == 0:
    print("Array does not contain any equi pair")

else:
    print("Indices which form equi pair {%d,%d}" % (i, j))
    print("Slices are {%d,%d},{%d,%d},{%d,%d}" % (0, i - 1, i + 1, j - 1, j + 1, N - 1))
