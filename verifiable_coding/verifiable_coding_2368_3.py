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
        # The target a and b must be such that for each gift, a_i >= target_a and b_i >= target_b
        # The target_a and target_b must be such that all a_i >= target_a and all b_i >= target_b
        # So target_a is the minimum of a_i, target_b is the minimum of b_i
        target_a = min(a)
        target_b = min(b)
        
        # Calculate the total moves needed
        moves = 0
        for i in range(n):
            moves += (a[i] - target_a)
            moves += (b[i] - target_b)
        
        results.append(str(moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()