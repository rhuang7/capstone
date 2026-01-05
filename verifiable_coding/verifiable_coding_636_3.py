import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    T = int(input[1])
    S = list(map(int, input[2:2+N]))
    
    count = 0
    from collections import defaultdict
    freq = defaultdict(int)
    for i in range(N):
        for j in range(i+1, N):
            s = S[i] + S[j]
            freq[s] += 1
    
    for i in range(N):
        for j in range(i+1, N):
            s = S[i] + S[j]
            rem = T - s
            if rem in freq:
                count += freq[rem]
    
    print(count)

if __name__ == '__main__':
    solve()