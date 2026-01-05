import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        zeros = a.count(0)
        nums = [x for x in a if x != 0]
        m = len(nums)
        if m + zeros != N:
            results.append(0)
            continue
        
        from itertools import permutations
        
        def is_good(p):
            cnt = 0
            for i in range(1, N):
                if p[i] > p[i-1]:
                    cnt += 1
            return cnt == K
        
        count = 0
        for perm in permutations(range(1, N+1)):
            if all(perm[i] == a[i] or a[i] == 0 for i in range(N)):
                if is_good(perm):
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()