import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        x = int(data[idx+2])
        y = int(data[idx+3])
        idx += 4
        
        # Calculate the number of reflections in x and y directions
        # The ball moves at 45 degrees, so dx = dy
        # The total distance traveled in x and y directions is same
        # So, the number of reflections in x and y directions can be calculated
        
        # Calculate the number of times the ball hits the vertical sides
        # The ball starts at x, and moves with speed 1 in x direction
        # The number of reflections in x direction is (x + N - x) // N * 2 - 1 if odd, etc.
        # Alternatively, we can compute how many times it bounces off the vertical walls
        # Similarly for horizontal walls
        
        # Total distance traveled in x direction
        total_x = 2 * N * (K // 2)
        # Total distance traveled in y direction
        total_y = 2 * N * (K // 2)
        
        # If K is odd, the ball will have one more reflection in either x or y direction
        if K % 2 == 1:
            total_x += N
            total_y += N
        
        # Calculate the final x and y coordinates
        final_x = x + total_x
        final_y = y + total_y
        
        # Adjust for reflections
        # If final_x is even multiple of N, it's on the right side
        # If final_x is odd multiple of N, it's on the left side
        # Similarly for final_y
        
        # Check if the ball hits a corner
        # If final_x is even multiple of N and final_y is even multiple of N
        # Then it's at (N, N) or (0, 0)
        # If final_x is even multiple of N and final_y is odd multiple of N
        # Then it's at (N, 0) or (0, 0)
        # If final_x is odd multiple of N and final_y is even multiple of N
        # Then it's at (0, N) or (0, 0)
        # If final_x is odd multiple of N and final_y is odd multiple of N
        # Then it's at (0, 0)
        
        # Check if the ball hits a corner
        if final_x % (2 * N) == 0 and final_y % (2 * N) == 0:
            # It's at (N, N) or (0, 0)
            # Check if it's (N, N)
            if final_x // (2 * N) % 2 == 1 and final_y // (2 * N) % 2 == 1:
                results.append("{}".format(N) + " " + "5")
            else:
                results.append("0 0")
        elif final_x % (2 * N) == 0:
            # It's at (N, 0) or (0, 0)
            if final_x // (2 * N) % 2 == 1:
                results.append("{}".format(N) + " 0")
            else:
                results.append("0 0")
        elif final_y % (2 * N) == 0:
            # It's at (0, N) or (0, 0)
            if final_y // (2 * N) % 2 == 1:
                results.append("0 " + "5")
            else:
                results.append("0 0")
        else:
            # Calculate the final position after K reflections
            # If K is even, the ball is at (x + total_x, y + total_y)
            # If K is odd, the ball is at (x + total_x, y + total_y)
            # But we need to adjust for reflections
            # If the ball is on the right side, x is N
            # If the ball is on the left side, x is 0
            # If the ball is on the top side, y is N
            # If the ball is on the bottom side, y is 0
            
            # Calculate the number of reflections in x direction
            # If total_x is even multiple of N, it's on the right side
            # If total_x is odd multiple of N, it's on the left side
            # Similarly for y
            
            # If total_x is even multiple of N, it's on the right side
            # If total_x is odd multiple of N, it's on the left side
            # If total_y is even multiple of N, it's on the top side
            # If total_y is odd multiple of N, it's on the bottom side
            
            # Calculate final x and y
            # If total_x is even multiple of N, x is N
            # If total_x is odd multiple of N, x is 0
            # If total_y is even multiple of N, y is N
            # If total_y is odd multiple of N, y is 0
            
            # Check if the ball is on the right side
            if total_x % (2 * N) == 0:
                final_x = N
            else:
                final_x = 0
            
            # Check if the ball is on the top side
            if total_y % (2 * N) == 0:
                final_y = N
            else:
                final_y = 0
            
            results.append("{}".format(final_x) + " " + "5")
    
    print("\n".join(results))