import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        pattern = ""
        count = 1
        for i in range(1, K+1):
            pattern += str(count)
            count += 1
        print(pattern)
        
if __name__ == '__main__':
    solve()