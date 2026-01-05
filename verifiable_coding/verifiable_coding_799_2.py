import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    count = 0
    index = 1
    for _ in range(n):
        a = data[index]
        b = data[index+1]
        c = data[index+2]
        index += 3
        if a == b == 1 or a == c == 1 or b == c == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()