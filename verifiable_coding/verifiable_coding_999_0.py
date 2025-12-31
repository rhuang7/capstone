import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        # Print the uppercase letters from A to the K-th letter
        for j in range(K):
            print(chr(ord('A') + j), end='')
        print()
        # Print numbers from 1 to K
        for j in range(1, K + 1):
            print(j, end='')
        print()

if __name__ == '__main__':
    solve()