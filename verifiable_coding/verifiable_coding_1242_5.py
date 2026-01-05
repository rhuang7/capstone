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
        # Because to reduce the array to one element, we need to remove N-1 elements
        # The cost of each operation is the smaller of the two elements
        # The optimal way is to always remove the larger element, which means the smaller one is added to the cost
        # So the total cost is the sum of all elements except the maximum
        min_cost = sum(A) - max(A)
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()