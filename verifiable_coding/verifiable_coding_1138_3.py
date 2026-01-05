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
        
        pos = [0] * (N + 1)  # pos[i] is the current position of person i
        steps = 0
        
        for i in range(1, N + 1):
            a = A[i - 1]
            if a == 0:
                # Person stands at the leftmost end
                pos[i] = 0
            else:
                # Person stands to the right of person a
                pos[i] = pos[a] + 1
            
            # Calculate the number of steps needed to insert person i
            # The person to the right of a (if any) must move right
            # The person to the left of i (if any) must move left
            # The minimal steps is the number of people between a and i
            # which is (i - a - 1)
            steps += (i - a - 1)
        
        results.append(str(steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()