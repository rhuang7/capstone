import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        R = int(data[index])
        C = int(data[index+1])
        index += 2
        print(R * C)

if __name__ == '__main__':
    solve()