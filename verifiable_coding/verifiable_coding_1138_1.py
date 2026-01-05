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
                steps += i - 1
                pos[i] = 0
            else:
                # Insert after a
                # The current position of a is pos[a]
                # The new position is pos[a] + 1
                # The number of steps needed is the number of people after a
                steps += (N - pos[a] - 1)
                pos[i] = pos[a] + 1
            # Update the positions of the people after the insertion point
            for j in range(i, N + 1):
                if pos[j] > pos[i]:
                    pos[j] += 1
        results.append(str(steps))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()