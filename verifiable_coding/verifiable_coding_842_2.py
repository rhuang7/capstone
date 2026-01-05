import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        for i in range(1, K+1):
            if i % 2 == 1:
                print(f"{i}   {i}")
            else:
                print(f"{i}{i}")
        print()

if __name__ == '__main__':
    solve()