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
        # Compute the minimal operations
        ops = []
        current_L, current_R = segments[0]
        for i in range(1, N):
            target_L, target_R = segments[i]
            # Move L to target_L
            diff_L = target_L - current_L
            for _ in range(abs(diff_L)):
                if diff_L > 0:
                    ops.append('L+')
                    current_L += 1
                else:
                    ops.append('L-')
                    current_L -= 1
            # Move R to target_R
            diff_R = target_R - current_R
            for _ in range(abs(diff_R)):
                if diff_R > 0:
                    ops.append('R+')
                    current_R += 1
                else:
                    ops.append('R-')
                    current_R -= 1
        # Calculate total operations
        total_ops = len(ops)
        # Find lexicographically minimal sequence
        # We already generate the minimal sequence by moving L first then R
        # So no need to adjust
        results.append(str(total_ops))
        results.append(''.join(ops))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()