import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    count = 0
    for i in range(2, 2 + n):
        if int(data[i]) % k == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()