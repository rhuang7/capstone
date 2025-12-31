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
        
        ops = 0
        for i in range(N - 1):
            if S[i] == S[i + 1]:
                ops += 1
                # Toggle the current bit
                S = S[:i] + ('1' if S[i] == '0' else '0') + S[i+1:]
        
        print(ops)

if __name__ == '__main__':
    solve()