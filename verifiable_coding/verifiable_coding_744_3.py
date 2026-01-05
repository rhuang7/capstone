import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print("*")
            print("*")
        else:
            for i in range(k):
                if i % 2 == 0:
                    print("*" * (k // 2 + 1))
                else:
                    print("* " * (k // 2) + "*")
            for i in range(k):
                if i % 2 == 0:
                    print("*" * (k // 2 + 1))
                else:
                    print("* " * (k // 2) + "*")
        if k != cases[-1]:
            print()