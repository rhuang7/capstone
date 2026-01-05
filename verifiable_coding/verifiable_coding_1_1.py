import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    results = []
    
    for _ in range(q):
        n = int(data[index])
        m = int(data[index+1])
        k = int(data[index+2])
        index += 3
        
        # Total distance
        total = n + m
        # Minimum moves required
        min_moves = max(n, m)
        # Maximum moves possible
        max_moves = n + m
        
        # Check if it's possible to reach in exactly k moves
        if k < min_moves or k > max_moves:
            results.append(-1)
            continue
        
        # Calculate the maximum number of diagonal moves
        # Diagonal moves contribute 2 units of distance
        # Non-diagonal moves contribute 1 unit of distance
        # Let d be the number of diagonal moves, and s be the number of straight moves
        # We have: 2d + s = total
        # And: d + s = k
        # Solving: d = k - s
        # Substitute: 2(k - s) + s = total => 2k - s = total => s = 2k - total
        # Since s must be >= 0, 2k >= total
        # Also, d = k - s = k - (2k - total) = total - k
        # So d = total - k
        # But d can't be more than k, so total - k <= k => total <= 2k
        # Which is already satisfied since k >= min_moves and min_moves >= total/2
        
        # So maximum diagonal moves is total - k
        # But we also need to ensure that the number of diagonal moves is feasible
        # Because each diagonal move contributes 2 units of distance, and we have total units
        # So the maximum possible diagonal moves is min(total, k)
        # But we also need to make sure that total - k is not more than k
        # Which is already satisfied
        
        # So the answer is total - k
        results.append(total - k)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()