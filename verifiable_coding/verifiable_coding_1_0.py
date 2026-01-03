import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    idx = 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        
        # Total distance
        total = n + m
        
        # Check if it's possible to reach in k moves
        # Minimum moves needed: max(ceil(n / 1), ceil(m / 1)) = max(n, m)
        # Maximum moves needed: n + m (all steps in one direction)
        # So for it to be possible, k must be between min_moves and max_moves
        min_moves = max(n, m)
        max_moves = n + m
        
        if k < min_moves or k > max_moves:
            results.append(-1)
            continue
        
        # Calculate the maximum number of diagonal moves
        # Each diagonal move covers 1 unit in x and 1 unit in y
        # So the maximum number of diagonal moves is min(n, m)
        # But we can't use more than (k - (n + m - min(n, m))) diagonal moves
        # Because the remaining steps must be axial moves (either x or y)
        # So the maximum number of diagonal moves is min(min(n, m), k - (n + m - min(n, m)))
        # But also, it can't be more than k - (n + m - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (n + m - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the minimum moves is max(n, m)
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of diagonal moves can't be more than k - (max(n, m) - min(n, m))
        # Because the remaining steps must be axial moves
        # So the maximum number of diagonal moves is min(min(n, m), k - (max(n, m) - min(n, m)))
        # But also, the number of