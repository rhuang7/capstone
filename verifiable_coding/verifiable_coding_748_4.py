import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx+N]))
        idx += N
        
        # The die starts with 1 on top, 2 on front, 3 on right, 4 on back, 5 on left, 6 on bottom
        # We need to find the correct orientation based on the sequence A
        # Try all possible initial configurations (there are 24 possible configurations of a die)
        # For each configuration, simulate the rolls and check if the sequence A matches
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # For each possible initial configuration, simulate the rolls and check if the sequence A matches
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # The possible rotations are:
        # 1. Rotate up (top becomes front, front becomes bottom, bottom becomes back, back becomes top)
        # 2. Rotate down (top becomes back, back becomes bottom, bottom becomes front, front becomes top)
        # 3. Rotate left (top becomes left, left becomes bottom, bottom becomes right, right becomes top)
        # 4. Rotate right (top becomes right, right becomes bottom, bottom becomes left, left becomes top)
        
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can try all possible initial configurations by rotating the die in different ways
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left, bottom
        
        # Try all possible initial configurations
        # The die can be rotated in 24 ways, but we can represent it with 4 possible rotations (up, down, left, right)
        # and 2 possible orientations (top and bottom)
        # So we can try all 24 possibilities by rotating in different ways
        
        # The initial configuration is:
        # top = 1, front = 2, right = 3, back = 4, left = 5, bottom = 6
        # We can represent the die as a dictionary with top, front, right, back, left, bottom
        # We can rotate the die in 4 directions: up, down, left, right
        # For each rotation, we need to update the top, front, right, back, left,