def tri(n):
    if n == 1: 
        return [0]
    if n == 2: 
        return [0,1]
    if n == 3: 
        return [0,1,1]
    t = tri(n-1)
    return t + [t[-1] + t[-2] + t[-3]]

N = int(input())
print(*tri(N))