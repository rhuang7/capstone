import sys
import itertools

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
        non_zeros = N - zeros
        missing = set(range(1, N+1)) - set(a)
        
        # Generate all permutations of the missing numbers
        missing_list = list(missing)
        for perm in itertools.permutations(missing_list):
            new_a = a.copy()
            pos = 0
            for i in range(N):
                if new_a[i] == 0:
                    new_a[i] = perm[pos]
                    pos += 1
            # Count the number of increasing positions
            cnt = 0
            for i in range(1, N):
                if new_a[i] > new_a[i-1]:
                    cnt += 1
            if cnt == K:
                results.append(1)
        results.append(sum(results[-zeros:]))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()