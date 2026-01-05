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
        # We'll use a list to track the current position of each person
        pos = [0] * (N + 1)  # pos[1] is the position of person 1, etc.
        steps = 0
        
        for i in range(1, N + 1):
            a = A[i - 1]
            if a == 0:
                # Person i goes to the leftmost end
                # So we need to move all people to the right of position 0 to the right
                # The number of steps is the number of people to the right of position 0
                steps += (N - i)
                pos[i] = 0
            else:
                # Person i goes to the right of person a
                # The target position is pos[a] + 1
                target = pos[a] + 1
                # We need to move all people to the right of target to the right
                # The number of steps is the number of people to the right of target
                steps += (N - target)
                pos[i] = target
        
        results.append(str(steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()