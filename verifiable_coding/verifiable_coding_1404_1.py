import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        R = int(data[index])
        G = int(data[index+1])
        B = int(data[index+2])
        index += 3
        K = int(data[index])
        index += 1
        
        # To ensure at least K balloons of the same color,
        # we need to consider the worst-case scenario where
        # we pick (K-1) balloons of each of the top two colors
        # and then one more to get the Kth of the third.
        # So, the minimum number is (K-1)*2 + 1
        # But we have to make sure that there are at least K balloons of one color.
        # So, if all colors have less than K, it's impossible, but according to constraints,
        # K is <= max(R, G, B), so it's always possible.
        min_balloons = (K - 1) * 2 + 1
        results.append(str(min_balloons))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()