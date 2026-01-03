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
                # Insert at the beginning
                steps += i - 1  # move all people to the left
                pos[i] = 0
            else:
                # Insert after person a
                # The current position of a is pos[a]
                # The new position is pos[a] + 1
                # To insert here, we need to move all people to the right of a to the right
                # The number of people to the right of a is (N - a)
                # But since we are inserting person i, the number of people to the right of a is (N - a - 1)
                # So steps += (N - a - 1)
                steps += (N - a - 1)
                pos[i] = pos[a] + 1
        
        results.append(str(steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()