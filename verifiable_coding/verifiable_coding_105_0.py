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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array in non-decreasing order
        a.sort()
        
        # Calculate the maximum number of operations
        total = 0
        for i in range(n-1, -1, -1):
            # We can add a[i] to all previous piles
            # But we need to make sure that the total doesn't exceed k
            # So we calculate how many times we can add a[i] to the previous piles
            # before the total exceeds k
            # The previous piles have total sum of (a[0] + a[1] + ... + a[i-1])
            # So the number of operations is (k - sum_prev) // a[i]
            # But we can only do this once per pile
            # So we take the minimum of (k - sum_prev) // a[i] and (i)
            # Because we can only add a[i] to i piles (all before it)
            sum_prev = sum(a[:i])
            ops = (k - sum_prev) // a[i]
            ops = min(ops, i)
            total += ops
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()