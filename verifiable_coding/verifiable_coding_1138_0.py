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
        
        # We will track the current positions of the people
        # Initially, person 1 is at position 0
        # For each new person, we find where they should be inserted
        # and calculate the number of steps needed
        # The steps are the number of people to the right of the insertion point
        # because we need to shift them to the right by 1
        # or the number of people to the left of the insertion point
        # because we need to shift them to the left by 1
        # We choose the minimum of the two
        
        # We will maintain a list of positions
        positions = [0]  # position of person 1
        
        total_steps = 0
        
        for i in range(1, N):
            a = A[i]
            if a == 0:
                # Insert at the beginning
                insert_pos = 0
            else:
                # Find the position of a
                insert_pos = positions[a - 1]
            
            # The new person will be inserted at insert_pos + 1
            # The number of people to the right of insert_pos is len(positions) - insert_pos - 1
            # The number of people to the left of insert_pos is insert_pos
            # We choose the minimum of these two
            steps = min(len(positions) - insert_pos - 1, insert_pos)
            total_steps += steps
            
            # Insert the new position
            positions.insert(insert_pos + 1, i)
        
        results.append(str(total_steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()