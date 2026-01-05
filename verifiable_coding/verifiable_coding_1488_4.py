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
        # that contain the given numbers in the correct positions
        # and have exactly K increasing positions
        count = 0
        for perm in itertools.permutations(range(1, N+1)):
            valid = True
            for i in range(N):
                if a[i] != 0 and a[i] != perm[i]:
                    valid = False
                    break
            if not valid:
                continue
            # Check the number of increasing positions
            inc = 0
            for i in range(1, N):
                if perm[i] > perm[i-1]:
                    inc += 1
            if inc == K:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()