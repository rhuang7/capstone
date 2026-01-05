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
        nums = [x for x in a if x != 0]
        m = len(nums)
        if m + zeros != N:
            results.append(0)
            continue
        
        # Generate all possible permutations of the numbers 1..N
        # That include the existing numbers in a, and fill the zeros with the missing numbers
        missing = set(range(1, N+1)) - set(nums)
        for perm in itertools.permutations(range(1, N+1)):
            # Check if the existing numbers are in the correct positions
            valid = True
            for i in range(N):
                if a[i] != 0 and a[i] != perm[i]:
                    valid = False
                    break
            if not valid:
                continue
            
            # Count the number of increasing positions
            inc = 0
            for i in range(1, N):
                if perm[i] > perm[i-1]:
                    inc += 1
            if inc == K:
                results.append(1)
        results.append(sum(results[-1]))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()