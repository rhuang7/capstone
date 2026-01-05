import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        n = len(S)
        max_len = 1
        
        for i in range(n):
            freq = {}
            left = i
            for j in range(i, n):
                freq[S[j]] = freq.get(S[j], 0) + 1
                if len(freq) <= 2:
                    max_len = max(max_len, j - i + 1)
        
        print(max_len)

if __name__ == '__main__':
    solve()