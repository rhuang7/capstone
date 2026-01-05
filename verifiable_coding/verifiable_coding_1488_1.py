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
        
        # Generate all permutations of the numbers 1..N
        all_perms = itertools.permutations(range(1, N+1))
        count = 0
        for p in all_perms:
            # Check if p can be formed by replacing zeros in a
            valid = True
            pos = 0
            for num in p:
                if a[pos] != 0 and a[pos] != num:
                    valid = False
                    break
                pos += 1
            if not valid:
                continue
            
            # Count the number of increasing positions
            inc = 0
            for i in range(1, N):
                if p[i] > p[i-1]:
                    inc += 1
            if inc == K:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()