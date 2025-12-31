import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    queries = list(map(int, data[2:2+M]))
    
    from collections import defaultdict

    # Precompute the frequency of each sum in C
    freq = defaultdict(int)
    for a in range(1, N + 1):
        for b in range(N + 1, 2 * N + 1):
            s = a + b
            freq[s] += 1

    for q in queries:
        print(freq.get(q, 0))

if __name__ == '__main__':
    solve()