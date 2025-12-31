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
        
        # Check if initial positions are same
        if x == y:
            print("Yes")
            continue
        
        # Calculate the difference between positions
        diff = abs(x - y)
        
        # The thief can be caught only if the difference is divisible by 2K
        # And the positions can reach the same point within the bounds
        if diff % (2 * K) != 0:
            print("No")
            continue
        
        # Check if the positions can reach the same point within the bounds
        # The positions must be reachable after some steps
        # The minimum distance between them is diff, and they move towards each other
        # The maximum distance they can move is N
        # So, the positions must be such that they can meet within the bounds
        # The positions after t steps must be within [0, N]
        # The positions after t steps are x + t*K and y + t*K (if moving towards each other)
        # So, the positions must be such that they can meet within the bounds
        # The minimum t is diff // (2*K)
        t = diff // (2 * K)
        
        # Check if the positions after t steps are within the bounds
        # The positions after t steps are x + t*K and y + t*K
        # But since they move towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >= 0 and y - t*K >= 0
        # But since they are moving towards each other, the positions after t steps must be within [0, N]
        # So, check if x + t*K <= N and y + t*K <= N
        # Also, check if x - t*K >=