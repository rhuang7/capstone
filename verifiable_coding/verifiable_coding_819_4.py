import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        if x == 1 and y == 1:
            print("YES")
        else:
            if (x - 1) % y == 0 or (y - 1) % x == 0:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()