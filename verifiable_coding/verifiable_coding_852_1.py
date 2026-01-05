import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T+1):
        K = int(input[i])
        pattern = []
        for j in range(K):
            if j % 2 == 0:
                pattern.append('0' if j == 0 else '1')
            else:
                pattern.append('1' if j == 0 else '0')
        print(''.join(pattern))

if __name__ == '__main__':
    solve()