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
        singers = []
        for _ in range(N):
            L = int(data[idx])
            U = int(data[idx+1])
            singers.append((L, U))
            idx += 2
        # Sort singers by L and U to find dominance
        singers.sort()
        # For each singer, find how many others are dominated by it
        scores = [0] * N
        for i in range(N):
            L_i, U_i = singers[i]
            count = 0
            for j in range(N):
                if i == j:
                    continue
                L_j, U_j = singers[j]
                # Check if singer i dominates singer j
                if L_j >= L_i and U_j <= U_i:
                    count += 1
            # Each dominated singer gives 2 points
            scores[i] = count * 2
        results.append(' '.join(map(str, scores)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()