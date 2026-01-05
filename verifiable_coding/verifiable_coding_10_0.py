import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the maximum possible sum of absolute differences
        max_sum = 0
        best_subsequence = []
        
        # Try all possible pairs
        for i in range(n):
            for j in range(i + 1, n):
                current_sum = abs(p[i] - p[j])
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_subsequence = [p[i], p[j]]
                elif current_sum == max_sum:
                    # Check if current subsequence is shorter
                    if len(best_subsequence) > 2:
                        best_subsequence = [p[i], p[j]]
        
        # If no pair found (should not happen as n >= 2)
        if len(best_subsequence) < 2:
            best_subsequence = p
        
        results.append(str(len(best_subsequence)))
        results.append(' '.join(map(str, best_subsequence)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()