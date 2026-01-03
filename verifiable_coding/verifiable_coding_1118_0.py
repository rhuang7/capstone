import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        
        operations = 0
        i = 0
        while i < N - 1:
            if S[i] == S[i + 1]:
                operations += 1
                S = S[:i] + str(1 - int(S[i])) + S[i+1:]
            i += 1
        
        print(operations)

if __name__ == '__main__':
    solve()