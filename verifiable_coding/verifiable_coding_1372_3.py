import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    index = 1
    for _ in range(n):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        dist_a = math.sqrt(x1**2 + y1**2)
        dist_b = math.sqrt(x2**2 + y2**2)
        if dist_a < dist_b:
            print("A IS CLOSER")
        else:
            print("B IS CLOSER")

if __name__ == '__main__':
    solve()