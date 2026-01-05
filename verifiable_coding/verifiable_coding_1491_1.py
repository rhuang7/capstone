import sys

def solve():
    data = sys.stdin.buffer.read().split()
    a, b, c, d = map(int, data)

    numbers = [a, b, c, d]
    for perm in range(24):
        x, y, z, w = numbers[perm//24], numbers[(perm//6)%4], numbers[(perm//4)%4], numbers[perm%4]
        if x * w == y * z:
            print("Possible")
            return
    print("Impossible")

if __name__ == '__main__':
    solve()