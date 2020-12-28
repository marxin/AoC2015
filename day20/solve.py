#!/usr/bin/env python3

minimum = 29000000

N = 2000000
a = [0] * N

for i in range(1, N):
    s = i
    while s < N:
        a[s] += 10 * i
        s += i

print(a[N - 1])
print(minimum)

for i in range(1, N):
    if a[i] >= minimum:
        print(i)
        break
