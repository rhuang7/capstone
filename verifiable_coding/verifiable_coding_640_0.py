import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[idx])
        Y = int(data[idx + 1])
        idx += 2
        
        if X == Y:
            results.append('0')
            continue
        
        # Find the minimum power such that X * (k) = Y * (k)
        # Which means k = max(X, Y) / min(X, Y)
        # But since k must be an integer, we find the least common multiple
        # of X and Y divided by the smaller of the two
        # So k = LCM(X, Y) / min(X, Y)
        # LCM(X, Y) = (X * Y) // GCD(X, Y)
        # So k = (X * Y) // GCD(X, Y) // min(X, Y)
        # Which simplifies to k = max(X, Y) // min(X, Y)
        # Because LCM(X, Y) / min(X, Y) = max(X, Y) / min(X, Y)
        # Only if one is a multiple of the other, else it's more complex
        # But in this case, we need the smallest k such that X*k = Y*k
        # Which is k = max(X, Y) // min(X, Y)
        # So the power required is k
        k = max(X, Y) // min(X, Y)
        results.append(str(k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()