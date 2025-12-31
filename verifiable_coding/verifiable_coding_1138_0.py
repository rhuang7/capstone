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
        
        # We'll keep track of the current positions of people
        # Initially, person 1 is at position 0 (leftmost)
        # We'll use a list to represent the current positions
        # Since people are added in order, we can track the positions
        # as we go
        positions = [0]  # position of person 1
        
        total_steps = 0
        
        for i in range(1, N):
            a_i = A[i]
            # Find the position of the person A[i]
            pos = positions[a_i]
            
            # The new position for person i is pos + 1
            # To insert at pos + 1, we need to shift people to the right
            # of pos to the right by 1
            # Or shift people to the left of pos to the left by 1
            # We choose the option that requires fewer steps
            # The number of people to the right of pos is (N - i)
            # The number of people to the left of pos is (pos)
            # So the minimal steps is min(pos, N - i)
            steps = min(pos, N - i)
            total_steps += steps
            
            # Update the positions
            # Shift people to the right of pos to the right by 1
            # So we insert at pos + 1
            positions.insert(pos + 1, i)
        
        results.append(str(total_steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()