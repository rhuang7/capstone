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
        N, P = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = (prefix[i] + A[i]) % P
        
        max_score = 0
        count = 0
        from collections import defaultdict
        freq = defaultdict(int)
        freq[0] = 1
        for i in range(N):
            current = prefix[i]
            target = (current - max_score) % P
            if target in freq:
                count += freq[target]
            if current > max_score:
                max_score = current
                freq = defaultdict(int)
                freq[current] = 1
            else:
                freq[current] += 1
        
        results.append(f"{max_score} {count}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()