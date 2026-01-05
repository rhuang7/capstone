import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        x = int(data[index])
        y = int(data[index+1])
        K = int(data[index+2])
        N = int(data[index+3])
        index += 4
        
        # Calculate the distance between x and y
        distance = abs(x - y)
        
        # The thief can be caught only if the distance is divisible by 2K
        # And the positions after moving are within the bounds [0, N]
        if distance % (2 * K) == 0:
            # Check if the positions after moving are within bounds
            # The positions after moving are x + K and x - K (for policeman)
            # Similarly for thief
            # But since they move optimally, we just need to check if the distance is divisible by 2K
            # And that the positions can be reached without going out of bounds
            # The minimal time is distance // (2 * K)
            # But the positions must be within 0 and N
            # So the positions after moving must be within 0 and N
            # So the initial positions must be such that x + K <= N and x - K >= 0
            # Similarly for y
            # But since x and y are within [0, N], and K <= N, it's possible
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()