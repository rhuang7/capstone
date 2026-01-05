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
        
        total_sum = sum(A)
        remaining_piles = N - X
        
        # The sum of remaining piles is total_sum - sum of removed piles
        # Since each move removes one pile, the sum of removed piles is sum of X smallest piles
        # So, sum of remaining piles = total_sum - sum of X smallest piles
        
        # Sort the array to get the X smallest piles
        A.sort()
        sum_removed = sum(A[:X])
        sum_remaining = total_sum - sum_removed
        
        if sum_remaining % 2 == 0:
            results.append("Jesse")
        else:
            results.append("Walter")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()