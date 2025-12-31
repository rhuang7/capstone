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
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = sum(A)
        remaining = N - X
        
        # The sum of the remaining piles is total - sum of removed piles
        # Since each move removes one pile, the sum of removed piles is sum of X smallest piles
        # So the sum of remaining piles is total - sum of X smallest piles
        
        # Sort the array
        A.sort()
        
        # Sum of X smallest piles
        sum_removed = sum(A[:X])
        sum_remaining = total - sum_removed
        
        if sum_remaining % 2 == 0:
            results.append("Jesse")
        else:
            results.append("Walter")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()