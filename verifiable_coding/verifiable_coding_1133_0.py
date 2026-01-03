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
        
        from collections import Counter
        freq = Counter(A)
        
        max_len = 0
        min_cost = float('inf')
        
        for length in freq:
            total = 0
            for a in A:
                total += a // length
            cost = total
            if cost < min_cost or (cost == min_cost and length > max_len):
                min_cost = cost
                max_len = length
        
        results.append(f"{max_len} {min_cost}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()