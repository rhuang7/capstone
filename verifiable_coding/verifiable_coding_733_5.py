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
        
        for i in range(N):
            # Check for odd length palindrome
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 < min_len or (r - l + 1 == min_len and s[l:r+1] < min_pal):
                    min_pal = s[l:r+1]
                    min_len = r - l + 1
                l -= 1
                r += 1
            
            # Check for even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 < min_len or (r - l + 1 == min_len and s[l:r+1] < min_pal):
                    min_pal = s[l:r+1]
                    min_len = r - l + 1
                l -= 1
                r += 1
        
        print(min_pal)

if __name__ == '__main__':
    solve()