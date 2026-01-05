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
        
        # Find the minimum number of balloons to ensure at least K of one color
        # Worst case: pick K-1 of each of the top two colors, then one more to get K of the third
        # So the answer is (K-1) * 2 + 1
        results.append((K-1)*2 + 1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()