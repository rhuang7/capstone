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
            U = int(data[idx + 1])
            singers.append((L, U))
            idx += 2
        # Sort singers by L and U to efficiently compare ranges
        singers.sort()
        # For each singer, find how many others are contained within it
        # and how many contain it
        scores = [0] * N
        for i in range(N):
            L_i, U_i = singers[i]
            # Find singers that are contained within i
            cnt_contained = 0
            # Find singers that contain i
            cnt_containing = 0
            for j in range(N):
                if i == j:
                    continue
                L_j, U_j = singers[j]
                # Check if i contains j
                if L_j >= L_i and U_j <= U_i:
                    cnt_contained += 1
                # Check if j contains i
                if L_i >= L_j and U_i <= U_j:
                    cnt_containing += 1
            # Add points
            scores[i] = cnt_contained * 2 + cnt_containing
        results.append(' '.join(map(str, scores)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()