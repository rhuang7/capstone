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
        
        # We will track the positions of the people
        # Initially, person 1 is at position 0
        positions = [0] * (N + 1)  # positions[0] unused
        positions[1] = 0
        
        total_steps = 0
        
        for i in range(2, N + 1):
            a = A[i - 1]
            # The desired position is positions[a] + 1
            desired_pos = positions[a] + 1
            # The current position of person i is i - 1 (since they are added in order)
            current_pos = i - 1
            
            # If desired position is to the left of current position, move people to the left
            if desired_pos < current_pos:
                # The number of steps is current_pos - desired_pos
                total_steps += current_pos - desired_pos
                # Move all people from desired_pos to current_pos - 1 to the left
                for j in range(desired_pos, current_pos):
                    positions[j] -= 1
                # Update the position of person i
                positions[i] = desired_pos
            else:
                # If desired position is to the right of current position, move people to the right
                # The number of steps is desired_pos - current_pos
                total_steps += desired_pos - current_pos
                # Move all people from current_pos to desired_pos - 1 to the right
                for j in range(current_pos, desired_pos):
                    positions[j] += 1
                # Update the position of person i
                positions[i] = desired_pos
        
        results.append(str(total_steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()