import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = data[index]
        R = data[index + 1]
        index += 2
        
        N = len(S)
        cost = 0
        k = 0
        l = 0
        
        i = 0
        while i < N:
            if S[i] != R[i]:
                # Start a new operation
                k += 1
                start = i
                while i < N and S[i] != R[i]:
                    i += 1
                end = i
                l += (end - start)
                cost += k * l
            else:
                i += 1
        
        print(cost)

if __name__ == '__main__':
    solve()