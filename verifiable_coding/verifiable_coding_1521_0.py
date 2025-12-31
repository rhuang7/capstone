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
        # Sort singers by lower bound and upper bound
        singers.sort()
        # For each singer, find how many others are contained within it
        scores = [0] * N
        for i in range(N):
            L_i, U_i = singers[i]
            count = 0
            for j in range(N):
                if i == j:
                    continue
                L_j, U_j = singers[j]
                if L_j >= L_i and U_j <= U_i:
                    count += 1
            scores[i] = count * 2
        # Now, for each pair (i, j), if i is not contained in j, and j is not contained in i, add 1 to each
        # To avoid O(N^2) time, we can precompute for each singer, the number of singers that are not contained in it and not containing it
        # But for now, we'll compute it directly
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                L_i, U_i = singers[i]
                L_j, U_j = singers[j]
                if L_j >= L_i and U_j <= U_i:
                    scores[i] += 2
                elif L_i >= L_j and U_i <= U_j:
                    scores[j] += 2
                else:
                    scores[i] += 1
                    scores[j] += 1
        results.append(' '.join(map(str, scores)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()