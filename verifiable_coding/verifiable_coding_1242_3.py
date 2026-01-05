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
        
        # The minimum cost is the sum of all elements except the maximum
        # Because in each operation, we remove the larger of two elements,
        # and the cost is the smaller one. To minimize the total cost,
        # we should remove all elements except the maximum, and the cost
        # of each operation is the smaller of the two, which is the minimum
        # of the two. So the total cost is the sum of all elements except
        # the maximum.
        max_val = max(A)
        total = sum(A) - max_val
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()