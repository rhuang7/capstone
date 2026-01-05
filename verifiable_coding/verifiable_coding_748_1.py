import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        if N == 1:
            results.append("-1")
            continue
        
        # Initial state: top=1, front=2, right=3, bottom=4, back=5, left=6
        # We need to find the initial configuration that matches the sequence A
        # Try all possible initial top faces (1-6)
        found = False
        for top in range(1, 7):
            # Initialize die state
            top_face = top
            front_face = 2
            right_face = 3
            bottom_face = 4
            back_face = 5
            left_face = 6
            
            # Opposite faces
            opp = [0] * 7
            opp[top_face] = bottom_face
            opp[bottom_face] = top_face
            opp[front_face] = back_face
            opp[back_face] = front_face
            opp[right_face] = left_face
            opp[left_face] = right_face
            
            # Check if the sequence matches
            current_top = top_face
            valid = True
            for i in range(N-1):
                # Determine direction based on the next top face
                next_top = A[i+1]
                if next_top == current_top:
                    # No change, invalid
                    valid = False
                    break
                # Determine direction
                if next_top == opp[current_top]:
                    # Opposite face, invalid
                    valid = False
                    break
                # Determine direction based on current top and next top
                if current_top == 1:
                    if next_top == 2:
                        # Roll front
                        new_top = 2
                        new_front = 1
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 3:
                        # Roll right
                        new_top = 3
                        new_front = 2
                        new_right = 1
                        new_bottom = 6
                        new_back = 5
                        new_left = 4
                    elif next_top == 4:
                        # Roll back
                        new_top = 4
                        new_front = 5
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                    elif next_top == 5:
                        # Roll left
                        new_top = 5
                        new_front = 4
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                elif current_top == 2:
                    if next_top == 1:
                        # Roll back
                        new_top = 1
                        new_front = 2
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 3:
                        # Roll right
                        new_top = 3
                        new_front = 2
                        new_right = 1
                        new_bottom = 6
                        new_back = 5
                        new_left = 4
                    elif next_top == 4:
                        # Roll front
                        new_top = 4
                        new_front = 2
                        new_right = 3
                        new_bottom = 6
                        new_back = 5
                        new_left = 1
                    elif next_top == 5:
                        # Roll left
                        new_top = 5
                        new_front = 4
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                elif current_top == 3:
                    if next_top == 1:
                        # Roll left
                        new_top = 1
                        new_front = 2
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 2:
                        # Roll back
                        new_top = 2
                        new_front = 3
                        new_right = 1
                        new_bottom = 6
                        new_back = 5
                        new_left = 4
                    elif next_top == 4:
                        # Roll front
                        new_top = 4
                        new_front = 3
                        new_right = 1
                        new_bottom = 6
                        new_back = 5
                        new_left = 2
                    elif next_top == 5:
                        # Roll right
                        new_top = 5
                        new_front = 4
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                elif current_top == 4:
                    if next_top == 1:
                        # Roll front
                        new_top = 1
                        new_front = 2
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 2:
                        # Roll back
                        new_top = 2
                        new_front = 4
                        new_right = 3
                        new_bottom = 6
                        new_back = 5
                        new_left = 1
                    elif next_top == 3:
                        # Roll right
                        new_top = 3
                        new_front = 4
                        new_right = 1
                        new_bottom = 6
                        new_back = 5
                        new_left = 2
                    elif next_top == 5:
                        # Roll left
                        new_top = 5
                        new_front = 4
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                elif current_top == 5:
                    if next_top == 1:
                        # Roll back
                        new_top = 1
                        new_front = 2
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 2:
                        # Roll front
                        new_top = 2
                        new_front = 5
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 4
                    elif next_top == 3:
                        # Roll left
                        new_top = 3
                        new_front = 5
                        new_right = 1
                        new_bottom = 6
                        new_back = 2
                        new_left = 4
                    elif next_top == 4:
                        # Roll right
                        new_top = 4
                        new_front = 5
                        new_right = 3
                        new_bottom = 6
                        new_back = 1
                        new_left = 2
                elif current_top == 6:
                    if next_top == 1:
                        # Roll left
                        new_top = 1
                        new_front = 2
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 6
                    elif next_top == 2:
                        # Roll back
                        new_top = 2
                        new_front = 6
                        new_right = 3
                        new_bottom = 4
                        new_back = 5
                        new_left = 1
                    elif next_top == 3:
                        # Roll front
                        new_top = 3
                        new_front = 6
                        new_right = 1
                        new_bottom = 4
                        new_back = 5
                        new_left = 2
                    elif next_top == 4:
                        # Roll right
                        new_top = 4
                        new_front = 6
                        new_right = 3
                        new_bottom = 5
                        new_back = 1
                        new_left = 2
                
                # Update current state
                current_top = new_top
                current_front = new_front
                current_right = new_right
                current_bottom = new_bottom
                current_back = new_back
                current_left = new_left
                
            if valid:
                # Output the opposite faces
                output = [0] * 7
                output[1] = opp[1]
                output[2] = opp[2]
                output[3] = opp[3]
                output[4] = opp[4]
                output[5] = opp[5]
                output[6] = opp[6]
                results.append(" ".join(map(str, output[1:7])))
                found = True
                break
        
        if not found:
            results.append("-1")
    
    for res in results:
        print(res)