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
        
        min_pal = s[0]
        for i in range(N):
            for j in range(i + 1, N + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    if len(substr) < len(min_pal) or (len(substr) == len(min_pal) and substr < min_pal):
                        min_pal = substr
        print(min_pal)

if __name__ == '__main__':
    solve()