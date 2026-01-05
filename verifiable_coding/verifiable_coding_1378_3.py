import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    A = int(input[0])
    N = int(input[1])
    K = int(input[2])
    
    chambers = [0] * K
    
    for _ in range(A):
        chambers[0] += 1
        i = 0
        while i < K:
            if chambers[i] > N:
                if i == K - 1:
                    break
                chambers[i] = 0
                chambers[i + 1] += 1
                i += 1
            else:
                i += 1
    
    print(' '.join(map(str, chambers)))

if __name__ == '__main__':
    solve()