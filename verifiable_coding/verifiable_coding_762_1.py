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
                    part = "1" * i
                else:
                    part = "0" * i
                pattern.append(part)
            result = " ".join(pattern)
            print(result)

if __name__ == '__main__':
    solve()