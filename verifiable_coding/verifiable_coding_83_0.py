import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        a = int(data[index+2])
        b = int(data[index+3])
        index += 4
        # The distance between the rabbits is y - x
        # Each second, the distance decreases by a + b
        # We need to check if the initial distance is divisible by (a + b)
        distance = y - x
        if (a + b) == 0:
            print(-1)
            continue
        if distance % (a + b) != 0:
            print(-1)
        else:
            print(distance // (a + b))

if __name__ == '__main__':
    solve()