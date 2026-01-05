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
        ops = []
        current_L, current_R = segments[0]
        for i in range(1, N):
            target_L, target_R = segments[i]
            # Move L to target_L
            while current_L < target_L:
                current_L += 1
                ops.append("L+")
            while current_L > target_L:
                current_L -= 1
                ops.append("L-")
            # Move R to target_R
            while current_R < target_R:
                current_R += 1
                ops.append("R+")
            while current_R > target_R:
                current_R -= 1
                ops.append("R-")
        results.append(f"{len(ops)}\n{''.join(ops)}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()