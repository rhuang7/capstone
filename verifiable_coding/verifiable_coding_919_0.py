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
        
        # Group consecutive equal elements
        groups = []
        prev = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == prev:
                count += 1
            else:
                groups.append(count)
                prev = A[i]
                count = 1
        groups.append(count)
        
        # Find the minimum number of operations
        min_ops = float('inf')
        for i in range(len(groups)):
            # Try to make this group even by deleting or inserting
            # If the group length is even, no operation is needed
            if groups[i] % 2 == 0:
                continue
            # Try to delete one element from this group
            # This will make it even if the group length is 1
            if groups[i] == 1:
                min_ops = min(min_ops, 1)
            # Try to delete one element from the previous group
            if i > 0:
                if groups[i-1] % 2 == 0:
                    min_ops = min(min_ops, 1)
                else:
                    min_ops = min(min_ops, 2)
            # Try to delete one element from the next group
            if i < len(groups) - 1:
                if groups[i+1] % 2 == 0:
                    min_ops = min(min_ops, 1)
                else:
                    min_ops = min(min_ops, 2)
            # Try to insert one element into this group
            min_ops = min(min_ops, 1)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()