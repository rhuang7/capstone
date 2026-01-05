import sys

def solve():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        A = int(data[index])
        B = int(data[index + 1])
        index += 2
        print(A + B)

if __name__ == '__main__':
    solve()