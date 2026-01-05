import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        if n == 1:
            print(m)
            continue
        # The time required is 2*m + (n-2)
        print(2 * m + (n - 2))

if __name__ == '__main__':
    solve()