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
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        sorted_A = sorted(A)
        sorted_B = sorted(B)
        
        if sorted_A != sorted_B:
            results.append("-1")
            continue
        
        # If already identical, cost is 0
        results.append("0")
    
    print("\n".join(results))