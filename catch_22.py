T = int(input())


def robomove(F, B, T, FD, BD):
    BD = BD * -1
    DT = 0
    TR = F - B
    Time = 0
    if TR > 0:
        while F != B:
            DT += F
            if DT >= FD:  # Ditch check
                Time += F - (DT - FD)
                break
            else:
                Time += F
                DT -= B
                Time += B

    if TR < 0:
        while F != B:
            DT += F
            Time += F
            DT -= B
            if DT <= BD:  # Ditch check
                Time += B - (abs(DT) - abs(BD))
                break
            else:
                Time += B * T

    if F == B:
        print("No Ditch")

    if DT > 0:
        print(f'{Time * T} F')

    if DT < 0:
        print(f'{Time * T} B')


array = []
for i in range(T):
    array.append([int(n) for n in input().split(" ")])

for i in range(0, T):
    robomove(array[i][0], array[i][1], array[i][2], array[i][3], array[i][4])

