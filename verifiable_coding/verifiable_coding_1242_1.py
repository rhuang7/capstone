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
        # Because we always remove the larger of two adjacent elements, and the cost is the smaller one.
        # The minimum total cost is achieved by always removing the larger element, and the cost is the smaller one.
        # The sum of all elements except the maximum is the minimum total cost.
        min_cost = sum(A) - max(A)
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()