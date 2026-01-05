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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find the minimum possible a_i and b_i for each gift
        # The final a_i and b_i must be such that a_i <= original a_i and b_i <= original b_i
        # Also, for each gift, a_i and b_i must be the same for all gifts
        # So, the final a_i and b_i must be the same for all gifts
        
        # The final a_i and b_i must be the same for all gifts, so we can find the minimum possible value for a_i and b_i
        # such that for all gifts, a_i <= original a_i and b_i <= original b_i, and a_i and b_i are the same for all gifts
        
        # The minimum possible a_i and b_i is the minimum of the original a_i and b_i for each gift
        # But we can't choose a_i and b_i independently, they must be the same for all gifts
        # So, we need to find the minimum value of x such that for all gifts, a_i >= x and b_i >= x
        
        # The minimum x is the minimum of the minimum of a_i and b_i for each gift
        min_x = min(min(a[i], b[i]) for i in range(n))
        
        # Now, calculate the total moves needed
        total_moves = 0
        
        for i in range(n):
            # For each gift, we need to reduce a_i and b_i to min_x
            # The number of moves is (a[i] - min_x) + (b[i] - min_x)
            total_moves += (a[i] - min_x) + (b[i] - min_x)
        
        results.append(str(total_moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()