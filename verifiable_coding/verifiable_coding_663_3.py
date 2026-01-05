import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        L = int(data[index])
        S = data[index + 1]
        index += 2
        
        min_str = S
        n = len(S)
        
        for i in range(L + 1):
            for j in range(i, n):
                substring = S[i:j]
                new_str = S[:i] + S[j:] + substring
                if new_str < min_str:
                    min_str = new_str
        
        print(min_str)

if __name__ == '__main__':
    solve()