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
        current_sum = 0
        for i in range(n):
            # We can add a[i] to all other piles (n-1 times)
            # But we need to ensure that after adding, the total doesn't exceed k
            # So the maximum number of times we can add a[i] is (k - current_sum) // a[i]
            # But we can't add more than (n-1) times (since there are n-1 other piles)
            max_ops = min((k - current_sum) // a[i], n - 1)
            total += max_ops
            current_sum += max_ops * a[i]
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()