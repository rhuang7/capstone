import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        count = 1
        for j in range(K):
            for k in range(j + 1):
                print(count, end='')
                count += 1
            print()
        print()

if __name__ == '__main__':
    solve()