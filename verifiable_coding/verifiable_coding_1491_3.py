import sys

def solve():
    data = sys.stdin.buffer.read().split()
    a, b, c, d = map(int, data)

    numbers = [a, b, c, d]
    for perm in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        x, y, z, w = numbers[perm//24], numbers[perm%24], numbers[perm//24+1], numbers[perm%24+1]
        if x * w == y * z:
            print("Possible")
            return
    print("Impossible")

if __name__ == '__main__':
    solve()