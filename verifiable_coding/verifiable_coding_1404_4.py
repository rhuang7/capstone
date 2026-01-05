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
        
        # Find the maximum of R, G, B
        max_color = max(R, G, B)
        # If K is larger than the maximum, it's impossible, but according to constraints, K <= max{R, G, B}
        # So we can safely compute
        # The minimum number of balloons needed is (K-1) * 3 + 1
        # Because in the worst case, we pick K-1 of each of the three colors, and then one more to get K of one color
        results.append((K-1)*3 + 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()