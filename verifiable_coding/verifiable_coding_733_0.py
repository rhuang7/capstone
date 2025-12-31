import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        N = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        min_pal = None
        min_len = float('inf')
        
        # Check all possible substrings of length 1
        for i in range(N):
            if min_len > 1:
                break
            if min_pal is None or s[i] < min_pal:
                min_pal = s[i]
                min_len = 1
        
        # Check all possible substrings of length 2
        for i in range(N - 1):
            if min_len > 2:
                break
            if s[i] == s[i + 1]:
                if min_pal is None or s[i:i+2] < min_pal:
                    min_pal = s[i:i+2]
                    min_len = 2
        
        # Check all possible substrings of length >= 3
        for l in range(3, N + 1):
            for i in range(N - l + 1):
                substr = s[i:i+l]
                if substr == substr[::-1]:
                    if min_pal is None or len(substr) < min_len or (len(substr) == min_len and substr < min_pal):
                        min_pal = substr
                        min_len = len(substr)
        
        print(min_pal)

if __name__ == '__main__':
    solve()