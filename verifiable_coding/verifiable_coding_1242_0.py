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
        # Because to reduce the array to one element, we must remove all other elements,
        # and the cost of each removal is the smaller of the two elements.
        # The optimal way is to always remove the larger element, so the cost is the smaller one.
        # The minimum total cost is the sum of all elements except the maximum.
        min_cost = sum(A) - max(A)
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()