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
        segments = []
        for _ in range(N):
            L = int(data[idx])
            R = int(data[idx + 1])
            segments.append((L, R))
            idx += 2
        if N == 1:
            results.append("0\n")
            continue
        current_L, current_R = segments[0]
        total_ops = 0
        operations = []
        for i in range(1, N):
            next_L, next_R = segments[i]
            # Calculate the difference between current and next
            delta_L = next_L - current_L
            delta_R = next_R - current_R
            # Move L first to make it lexicographically minimal
            for _ in range(delta_L):
                operations.append("L+")
                current_L += 1
            # Move R next
            for _ in range(delta_R):
                operations.append("R+")
                current_R += 1
            # Now move L again to make it lexicographically minimal
            for _ in range(delta_L):
                operations.append("L+")
                current_L += 1
            # Now move R again
            for _ in range(delta_R):
                operations.append("R+")
                current_R += 1
            total_ops += 2 * (delta_L + delta_R)
        results.append(f"{total_ops}\n{''.join(operations)}")
    print('\n'.join(results))