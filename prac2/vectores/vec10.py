def cnt_rep(v):
    f = {}
    for x in v:
        f[x] = f.get(x,0)+1
    return f

def max_rep(f):
    m = max(f.values())
    return [n for n,c in f.items() if c==m]

n = int(input())
nums = list(map(int,input().split()))

f = cnt_rep(nums)
mr = max_rep(f)

print(' '.join(map(str,sorted(mr))))