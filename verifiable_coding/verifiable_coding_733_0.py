import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        min_pal = None
        min_len = float('inf')
        
        for i in range(N):
            for j in range(i, N):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    if len(substring) < min_len or (len(substring) == min_len and substring < min_pal):
                        min_pal = substring
                        min_len = len(substring)
        
        print(min_pal)

if __name__ == '__main__':
    solve()