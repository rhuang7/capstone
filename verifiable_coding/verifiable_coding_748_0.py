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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        if N == 1:
            results.append("-1")
            continue
        
        # Initial state: top=1, front=2, right=3, bottom=4, back=5, left=6
        # We need to find the correct initial configuration
        # Try all possible initial configurations
        from itertools import permutations
        for top, front, right, bottom, back, left in permutations(range(1,7)):
            # Initialize die
            top_face = top
            front_face = front
            right_face = right
            bottom_face = bottom
            back_face = back
            left_face = left
            
            # Opposite faces
            opposite = [0] * 7
            opposite[top] = bottom
            opposite[bottom] = top
            opposite[front] = back
            opposite[back] = front
            opposite[right] = left
            opposite[left] = right
            
            # Check if the sequence A matches
            valid = True
            current_top = top_face
            current_front = front_face
            current_right = right_face
            current_bottom = bottom_face
            current_back = back_face
            current_left = left_face
            
            for i in range(N-1):
                # Determine direction based on the change in top face
                # For each possible direction, simulate the roll
                # We need to find the correct direction that leads to the next top face
                # Try all 4 directions
                # Direction 1: roll forward (top becomes front, front becomes bottom, bottom becomes back, back becomes top)
                # Direction 2: roll backward (top becomes back, back becomes bottom, bottom becomes front, front becomes top)
                # Direction 3: roll right (top becomes right, right becomes bottom, bottom becomes left, left becomes top)
                # Direction 4: roll left (top becomes left, left becomes bottom, bottom becomes right, right becomes top)
                
                # Try all 4 directions
                found = False
                for direction in [1, 2, 3, 4]:
                    if direction == 1:
                        # Roll forward
                        new_top = current_front
                        new_front = current_bottom
                        new_bottom = current_back
                        new_back = current_top
                        new_right = current_right
                        new_left = current_left
                    elif direction == 2:
                        # Roll backward
                        new_top = current_back
                        new_back = current_top
                        new_top = current_back
                        new_back = current_top
                        new_front = current_bottom
                        new_bottom = current_front
                        new_right = current_right
                        new_left = current_left
                    elif direction == 3:
                        # Roll right
                        new_top = current_right
                        new_right = current_bottom
                        new_bottom = current_left
                        new_left = current_top
                        new_front = current_front
                        new_back = current_back
                    elif direction == 4:
                        # Roll left
                        new_top = current_left
                        new_left = current_top
                        new_top = current_left
                        new_left = current_top
                        new_right = current_right
                        new_bottom = current_front
                        new_front = current_bottom
                        new_back = current_back
                    
                    # Check if the new top matches the next value in A
                    if new_top == A[i+1]:
                        # Update the current state
                        current_top = new_top
                        current_front = new_front
                        current_right = new_right
                        current_bottom = new_bottom
                        current_back = new_back
                        current_left = new_left
                        found = True
                        break
                if not found:
                    valid = False
                    break
            
            if valid:
                # Build the opposite array
                res = [0] * 7
                res[top] = bottom
                res[bottom] = top
                res[front] = back
                res[back] = front
                res[right] = left
                res[left] = right
                # Output the opposite of 1 to 6
                output = ' '.join(str(res[i]) for i in range(1,7))
                results.append(output)
                break
        else:
            results.append("-1")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()