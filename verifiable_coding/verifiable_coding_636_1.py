import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    T = int(data[1])
    S = list(map(int, data[2:2+N]))
    
    count = 0
    from collections import defaultdict

    # Precompute all possible sums of two elements
    sum2 = defaultdict(int)
    for i in range(N):
        for j in range(i+1, N):
            sum2[S[i] + S[j]] += 1

    # For each pair of sums, check if their combined sum equals T
    for s1 in sum2:
        for s2 in sum2:
            if s1 + s2 == T:
                count += sum2[s1] * sum2[s2]

    print(count)

if __name__ == '__main__':
    solve()