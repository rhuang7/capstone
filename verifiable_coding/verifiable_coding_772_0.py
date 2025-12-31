import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        N = len(S)
        count = 0
        
        # Each single element is a valid sequence
        count += N
        
        # For each position i, check sequences starting at i with p > 1
        for i in range(N):
            j = i + 1
            while j < N:
                if S[i] == S[j]:
                    count += 1
                p = 2
                while True:
                    next_j = j * p
                    if next_j >= N:
                        break
                    if S[j] == S[next_j]:
                        count += 1
                    j = next_j
                    p += 1
        
        print(count)

if __name__ == '__main__':
    solve()