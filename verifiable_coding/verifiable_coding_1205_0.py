import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        total = 0
        
        # For each possible pair of indices (i, i+1)
        for i in range(n - 1):
            # Original characters
            a = S[i]
            b = S[i + 1]
            
            # Count how many times (a, b) and (b, a) appear in the original string
            # For each occurrence of (a, b) or (b, a), it contributes 1 to the total
            # But we need to consider all possible (L, R) ranges that include this pair
            # So we count the number of (L, R) ranges that include this pair
            # Which is (i + 1) * (n - i)
            count = (i + 1) * (n - i)
            
            # If a == b, then this pair contributes 1 to F(S, L, R) for all (L, R) that include it
            # So we add count to the total
            if a == b:
                total += count
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()