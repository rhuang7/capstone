import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    T = int(input[idx])
    idx += 1
    S = list(map(int, input[idx:idx+N]))
    
    count = 0
    from collections import defaultdict
    freq = defaultdict(int)
    for i in range(N):
        for j in range(i+1, N):
            sum_ij = S[i] + S[j]
            freq[sum_ij] += 1
    
    for i in range(N):
        for j in range(i+1, N):
            sum_ij = S[i] + S[j]
            target = T - sum_ij
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if S[k] + S[l] == target:
                        count += 1
    
    print(count)

if __name__ == '__main__':
    solve()