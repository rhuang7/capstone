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
            R = int(data[idx+1])
            segments.append((L, R))
            idx += 2
        if N == 1:
            results.append("0\n")
            continue
        ops = []
        current_L, current_R = segments[0]
        for i in range(1, N):
            target_L, target_R = segments[i]
            # Calculate the difference
            delta_L = target_L - current_L
            delta_R = target_R - current_R
            # Move L first to ensure lex order
            for _ in range(delta_L):
                ops.append("L+")
                current_L += 1
            for _ in range(delta_R):
                ops.append("R+")
                current_R += 1
            # Now move back to ensure lex order
            for _ in range(delta_L):
                ops.append("L-")
                current_L -= 1
            for _ in range(delta_R):
                ops.append("R-")
                current_R -= 1
        results.append(f"{len(ops)}\n{''.join(ops)}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()