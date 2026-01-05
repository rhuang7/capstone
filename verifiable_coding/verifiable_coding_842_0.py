import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        for i in range(1, k+1):
            if i % 2 == 1:
                print(str(i) + ' ' * (2*(k//2 - (i//2))) + str(i))
            else:
                print(str(i) * 2)
        print()

if __name__ == '__main__':
    solve()