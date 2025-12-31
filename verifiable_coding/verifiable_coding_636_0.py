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

    # For each pair of sums, check if the remaining sum is T - sum1
    for sum1 in sum2:
        target = T - sum1
        for sum2_val in sum2:
            if sum1 + sum2_val == T:
                count += sum2[sum1] * sum2[sum2_val]

    print(count)

if __name__ == '__main__':
    solve()