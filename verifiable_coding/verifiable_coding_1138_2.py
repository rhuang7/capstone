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
        
        # We'll track the positions of each person
        # Initially, person 1 is at position 0
        pos = [0] * (N + 1)  # pos[1] is position of person 1, etc.
        steps = 0
        
        for i in range(1, N + 1):
            a = A[i - 1]
            if a == 0:
                # Person i stands at the leftmost end
                # All people to the right of position 0 must move right
                steps += (i - 1)
                pos[i] = 0
            else:
                # Person i stands to the right of person a
                # The desired position is pos[a] + 1
                desired_pos = pos[a] + 1
                # The current position of person i is i - 1 (since they are added in order)
                # If desired_pos < current position, we need to move people to the left
                # If desired_pos > current position, we need to move people to the right
                # We choose the minimal steps by moving the smaller group
                if desired_pos < i - 1:
                    # Move people to the left
                    steps += (i - 1 - desired_pos)
                    pos[i] = desired_pos
                else:
                    # Move people to the right
                    steps += (desired_pos - (i - 1))
                    pos[i] = desired_pos
        
        results.append(str(steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()