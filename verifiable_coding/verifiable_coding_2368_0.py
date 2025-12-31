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
        
        # Find the minimum possible value for a_i and b_i
        # The final a_i and b_i must be <= min(a), min(b)
        # But we can also decrease some of them to make them equal
        # So the final a_i and b_i must be such that a_i <= min(a), b_i <= min(b)
        # And a_i and b_i must be the same for all gifts
        
        # The minimum possible value for a_i and b_i is the minimum of all a_i and b_i
        min_a = min(a)
        min_b = min(b)
        
        # The final a_i and b_i must be such that a_i <= min_a and b_i <= min_b
        # And a_i and b_i must be the same for all gifts
        # So the final a_i and b_i can be any value between 0 and min(min_a, min_b)
        # But we need to find the optimal value to minimize the total moves
        
        # We can try all possible values of x (final a_i and b_i)
        # x can be from 0 to min(min_a, min_b)
        # For each x, calculate the total moves needed
        # The optimal x is the one that gives the minimum total moves
        
        min_total = float('inf')
        max_x = min(min_a, min_b)
        
        for x in range(0, max_x + 1):
            total = 0
            for i in range(n):
                # For a_i: need to reduce from a[i] to x
                # Each reduction can be done by eating 1 candy (cost 1) or 1 candy and 1 orange (cost 1)
                # So the minimum cost to reduce a[i] to x is (a[i] - x)
                # Similarly for b[i]
                total += (a[i] - x) + (b[i] - x)
            
            min_total = min(min_total, total)
        
        results.append(str(min_total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()