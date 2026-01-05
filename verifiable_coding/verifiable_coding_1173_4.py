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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        prefix_xor = [0] * (N + 1)
        for i in range(N):
            prefix_xor[i + 1] = prefix_xor[i] ^ A[i]
        
        count = 0
        freq = {}
        for i in range(N + 1):
            x = prefix_xor[i]
            if x in freq:
                count += freq[x]
            else:
                freq[x] = 0
            freq[x] += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()