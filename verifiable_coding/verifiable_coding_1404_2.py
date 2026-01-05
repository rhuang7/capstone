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
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        idx += 3
        K = int(data[idx])
        idx += 1
        
        # To ensure at least K balloons of the same color,
        # we need to consider the worst case where we pick
        # (K-1) balloons of each of the top two colors,
        # and then one more to get K of the third.
        # So the minimum number is (K-1)*2 + 1
        # But we also need to check if any of the colors has at least K.
        min_balloons = 0
        max_color = max(R, G, B)
        if max_color >= K:
            min_balloons = K
        else:
            min_balloons = (K - 1) * 2 + 1
        
        results.append(str(min_balloons))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()