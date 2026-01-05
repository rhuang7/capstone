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
        N = int(data[idx])
        idx += 1
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if the target color is the same for all positions
        target = C[0]
        same = all(c == target for c in C)
        if same:
            results.append("Yes")
            continue
        
        # Check if there's a way to paint the canvas with the brush
        # The brush can paint 3 consecutive millimeters at a time
        # So, the target must be achievable by overlapping brush strokes
        # We need to find a way to cover all positions with brush strokes
        # such that each position is covered by at least one brush stroke
        # and the color of each position matches the target
        
        # Check if the first 3 positions are all the same
        if C[0] == C[1] == C[2]:
            results.append("Yes")
            continue
        
        # Check if the last 3 positions are all the same
        if C[-3] == C[-2] == C[-1]:
            results.append("Yes")
            continue
        
        # Check if there's a position where the color is different from the target
        # and it's not at the start or end of the canvas
        # because the brush can't paint just the first or last 1 or 2 millimeters
        # So, if there's a position i (1 <= i <= N-2) where C[i] != target, then it's impossible
        # because the brush can't paint just that position
        # So, we need to check if all positions except possibly the first two and last two are the same as target
        # and the first three and last three are also the same as target
        # Because the brush can paint the first three and the last three, and the middle part can be covered by overlapping strokes
        
        # Check if the first three and last three are the same as target
        # and the middle part is also the same as target
        # But this is already checked above
        # So, if the first three and last three are not the same as target, then it's impossible
        # So, we need to check if the first three and last three are the same as target
        # and the middle part is also the same as target
        # But this is already checked above
        
        # If none of the above, then it's impossible
        results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()