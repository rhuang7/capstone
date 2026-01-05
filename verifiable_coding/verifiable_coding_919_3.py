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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Group the sequence into runs of equal elements
        runs = []
        current_val = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == current_val:
                count += 1
            else:
                runs.append(count)
                current_val = A[i]
                count = 1
        runs.append(count)
        
        # Find the minimum number of operations
        min_ops = float('inf')
        
        # Try all possible ways to make the sequence even
        # We can either delete elements or insert elements
        # The optimal way is to make all runs have even length
        
        # Try to make all runs even
        for i in range(len(runs)):
            if runs[i] % 2 != 0:
                # We can either delete one element or insert one element
                # To minimize operations, we choose the option with fewer operations
                # Delete one element: cost is 1
                # Insert one element: cost is 1
                # So, the cost is 1
                min_ops = min(min_ops, 1)
        
        # If all runs are even, the sequence is already even
        # So, the cost is 0
        if all(r % 2 == 0 for r in runs):
            min_ops = 0
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()