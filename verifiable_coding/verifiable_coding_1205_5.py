import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        S = data[idx]
        idx += 1
        
        n = len(S)
        total = 0
        
        # For each pair of consecutive characters (i, i+1)
        # Count how many times they are the same in all possible (L, R) intervals
        # where i is in [L, R]
        for i in range(n - 1):
            if S[i] == S[i + 1]:
                # The number of intervals (L, R) where L <= i and R >= i+1
                # is (i + 1) * (n - i)
                total += (i + 1) * (n - i)
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()