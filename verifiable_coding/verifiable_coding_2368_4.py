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
        
        # Find the minimum possible value for a_i and b_i after operations
        # The target a_i must be <= min(a), and target b_i must be <= min(b)
        # But we can also decrease some values to make them equal
        # So we need to find the minimum possible target a and b such that all a_i >= target a and all b_i >= target b
        
        # For each gift, the maximum possible target a is min(a), and similarly for b
        # But we can also decrease some values to make them equal
        
        # The minimum number of moves is the sum of:
        # (a_i - target_a) + (b_i - target_b) for all i
        # But target_a and target_b must be such that target_a <= a_i and target_b <= b_i for all i
        
        # We can try all possible target_a and target_b values
        # But since a_i and b_i can be up to 1e9, we need an efficient way
        
        # The optimal target_a is the minimum of a_i, and target_b is the minimum of b_i
        # But this may not be the optimal solution, because we can decrease some a_i and b_i to make them equal
        
        # So we need to find the optimal target_a and target_b such that:
        # target_a <= a_i for all i
        # target_b <= b_i for all i
        # and target_a = target_b
        
        # So the target must be the minimum of the minimum of a and b
        # But we can also decrease some values to make them equal
        
        # So the optimal target is the minimum of the minimum of a and b
        
        min_a = min(a)
        min_b = min(b)
        target = min(min_a, min_b)
        
        # Now calculate the number of moves
        moves = 0
        for i in range(n):
            moves += (a[i] - target)
            moves += (b[i] - target)
        
        results.append(str(moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()