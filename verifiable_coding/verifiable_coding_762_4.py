import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        if K == 1:
            print("1 ")
        else:
            pattern = []
            for i in range(1, K+1):
                if i % 2 == 1:
                    part = "1" + "0"*(i-1)
                else:
                    part = "0"*(i-1) + "1"
                pattern.append(part)
            print(" ".join(pattern))
            
if __name__ == '__main__':
    solve()