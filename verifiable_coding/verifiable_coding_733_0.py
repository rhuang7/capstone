import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        S = data[index + 1]
        index += 2
        
        min_pal = None
        min_len = float('inf')
        
        # Check all possible substrings of length 1
        for i in range(N):
            if min_len > 1:
                break
            if S[i] < min_pal or (min_len == 1 and min_pal is None):
                min_pal = S[i]
                min_len = 1
        
        # Check all possible substrings of length 2
        for i in range(N - 1):
            if S[i] == S[i + 1]:
                if min_len > 2:
                    break
                if (min_len == 2 and min_pal is None) or (min_len == 2 and S[i:i+2] < min_pal):
                    min_pal = S[i:i+2]
                    min_len = 2
        
        # Check all possible substrings of length >= 3
        for length in range(3, N + 1):
            for i in range(N - length + 1):
                substring = S[i:i+length]
                if substring == substring[::-1]:
                    if min_len > length:
                        min_pal = substring
                        min_len = length
                    elif min_len == length:
                        if substring < min_pal:
                            min_pal = substring
        
        print(min_pal)

if __name__ == '__main__':
    solve()