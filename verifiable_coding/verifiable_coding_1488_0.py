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
        
        # Generate all possible permutations of the missing numbers
        missing_list = list(missing)
        permutations = itertools.permutations(missing_list)
        
        count = 0
        for perm in permutations:
            new_a = a.copy()
            for i in range(N):
                if new_a[i] == 0:
                    new_a[i] = perm[0]
                    perm = perm[1:]
            # Check if new_a is a permutation of 1..N
            if set(new_a) == set(range(1, N+1)):
                # Count the number of increasing positions
                inc = 0
                for i in range(1, N):
                    if new_a[i] > new_a[i-1]:
                        inc += 1
                if inc == K:
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()