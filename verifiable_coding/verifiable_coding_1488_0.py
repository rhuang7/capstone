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
        # But we need to insert the missing numbers (those not in nums) into the zeros
        # So first, find the missing numbers
        missing = [x for x in range(1, N+1) if x not in nums]
        # Now, we need to insert these missing numbers into the zeros
        # For each possible way to insert the missing numbers into the zeros, we get a sequence
        # Then, for each such sequence, count the number of increasing positions
        
        total = 0
        for perm in itertools.permutations(missing):
            # Create a new list with the numbers and the perm inserted into the zeros
            new_a = []
            zero_count = 0
            for x in a:
                if x == 0:
                    zero_count += 1
                    new_a.append(perm[zero_count-1])
                else:
                    new_a.append(x)
            
            # Now, count the number of increasing positions
            cnt = 0
            for i in range(1, N):
                if new_a[i] > new_a[i-1]:
                    cnt += 1
            if cnt == K:
                total += 1
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()