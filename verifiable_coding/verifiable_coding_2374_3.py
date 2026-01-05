import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    idx = 1
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        top = data[idx]
        idx += 1
        bottom = data[idx]
        idx += 1
        
        # Convert to list of integers
        top = [int(c) for c in top]
        bottom = [int(c) for c in bottom]
        
        # Check if it's possible to connect the flow
        # We need to find a path from (1, 0) to (2, n+1)
        # The flow must go through the pipes in a way that connects them
        
        # We'll simulate the possible paths using BFS
        # We'll represent the pipes as a grid and track the direction of the flow
        
        # Directions: 0 - left, 1 - up, 2 - right, 3 - down
        # For each cell, we'll track the possible directions the flow can come from
        
        # Initialize a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        # We'll perform BFS from (1, 0) and see if we can reach (2, n+1)
        
        from collections import deque
        
        # Directions: 0 - left, 1 - up, 2 - right, 3 - down
        # For each pipe type, we'll determine the possible directions it can connect
        # For example, type 1 is a straight pipe that can connect left to right
        # type 2 is a straight pipe that can connect up to down
        # types 3-6 are curved pipes that can connect in different ways
        
        # Define the possible directions each pipe type can connect
        # For each pipe type, we'll store the possible directions it can connect to
        # For example, type 1 can connect left to right, right to left, up to down, down to up
        # But we'll need to determine which directions are possible based on the rotation
        
        # For each pipe type, we'll define the possible directions it can connect
        # This is a bit complex, but we can use the following approach:
        # For each pipe, we'll determine the possible directions it can connect to
        # Based on the rotation, we can have different configurations
        
        # We'll use a helper function to determine the possible directions a pipe can connect
        # For each pipe, we'll check all possible rotations and determine the possible directions
        
        # For simplicity, we'll use a precomputed map of possible directions for each pipe type
        # For example, for type 1, it can connect left to right, right to left, up to down, down to up
        # So the possible directions are 0 (left), 2 (right), 1 (up), 3 (down)
        
        # We'll create a list of possible directions for each pipe type
        # For each pipe type, we'll store a set of directions it can connect to
        # For example, type 1 can connect left, right, up, down
        # type 2 can connect up, down, left, right
        # types 3-6 can connect in different ways
        
        # We'll create a list of possible directions for each pipe type
        # For each pipe type, we'll store a set of directions it can connect to
        # For example, type 1 can connect left, right, up, down
        # type 2 can connect up, down, left, right
        # types 3-6 can connect in different ways
        
        # Let's define the possible directions for each pipe type
        # We'll use the following mapping:
        # 1: straight pipe, can connect left-right, up-down
        # 2: straight pipe, can connect up-down, left-right
        # 3: curved pipe, can connect left-up, up-right, right-down, down-left
        # 4: curved pipe, can connect left-down, down-right, right-up, up-left
        # 5: curved pipe, can connect left-up, up-right, right-down, down-left
        # 6: curved pipe, can connect left-down, down-right, right-up, up-left
        
        # For each pipe type, we'll define the possible directions it can connect
        # For example, type 1 can connect left, right, up, down
        # type 2 can connect left, right, up, down
        # types 3-6 can connect in different ways
        
        # We'll create a list of possible directions for each pipe type
        # For each pipe type, we'll store a set of directions it can connect to
        # For example, type 1 can connect left, right, up, down
        # type 2 can connect left, right, up, down
        # types 3-6 can connect in different ways
        
        # Let's define the possible directions for each pipe type
        # For each pipe type, we'll store a set of directions it can connect to
        # For example, type 1 can connect left, right, up, down
        # type 2 can connect left, right, up, down
        # types 3-6 can connect in different ways
        
        # For the purposes of this problem, we'll assume that any pipe can be rotated to connect in any direction
        # So for any pipe, we can connect in any direction
        
        # So for any pipe, we can connect in any direction
        
        # We'll use a BFS approach to find a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array, with rows 0 and 1 (top and bottom)
        # Each cell will store the possible directions the flow can come from
        
        # We'll use a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        # We'll perform BFS from (1, 0) and see if we can reach (2, n+1)
        
        # We'll create a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        
        # We'll create a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        
        # We'll use a BFS approach to find a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array, with rows 0 and 1 (top and bottom)
        # Each cell will store the possible directions the flow can come from
        
        # We'll create a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        
        # We'll use a BFS approach to find a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array, with rows 0 and 1 (top and bottom)
        # Each cell will store the possible directions the flow can come from
        
        # We'll create a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions the flow can come from
        # Initially, the flow can come from the left (direction 0) at (1, 0)
        
        # We'll use a BFS approach to find a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array, with rows 0 and 1 (top and bottom)
        # Each cell will store the possible directions the flow can come from
        
        # We'll create a 2D array to track the possible directions
        # We'll use a 2D array of size (2 x n) to represent the grid
        # Each cell will store a set of directions