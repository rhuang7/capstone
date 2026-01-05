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
        
        # Check if the target color can be achieved with brush size 3
        # The brush can paint 3 consecutive millimeters at a time
        # So, the target color must be the same in every 3 consecutive positions
        # But since the brush can be applied multiple times, it's possible to paint overlapping regions
        # So, the only constraint is that the color in each position must be the same as the color in the position 3 steps ahead
        
        # Check if the color sequence is valid
        valid = True
        for i in range(N - 2):
            if C[i] != C[i + 3]:
                valid = False
                break
        
        results.append("Yes" if valid else "No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()