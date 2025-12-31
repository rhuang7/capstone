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
        # Because in each operation, we remove the larger of two elements, and the cost is the smaller one.
        # To minimize the total cost, we should always remove the larger element, which means the smaller one is added to the cost.
        # The minimum total cost is the sum of all elements except the maximum, since the maximum will be the last element left.
        min_cost = sum(A) - max(A)
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()