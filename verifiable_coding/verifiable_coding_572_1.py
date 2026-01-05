import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        K = int(data[index+2])
        index += 3
        
        # Calculate the current difference
        diff = abs(N - M)
        
        # Use the coins to minimize the difference
        # The maximum we can reduce the difference is K (if we have enough coins)
        # But the minimum possible difference is max(0, diff - K)
        min_diff = max(0, diff - K)
        print(min_diff)

if __name__ == '__main__':
    solve()