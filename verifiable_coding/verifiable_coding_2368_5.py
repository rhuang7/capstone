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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the minimum possible a_i and b_i for all gifts
        min_a = min(a)
        min_b = min(b)
        
        # Calculate the total moves needed
        total_moves = 0
        
        for i in range(n):
            # For candies
            total_moves += (a[i] - min_a)
            # For oranges
            total_moves += (b[i] - min_b)
        
        results.append(str(total_moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()