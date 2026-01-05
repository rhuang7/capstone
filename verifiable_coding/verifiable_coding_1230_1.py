import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    for i in range(n - 3):
        a = A[i]
        b = A[i + 1]
        c = A[i + 2]
        d = A[i + 3]
        if (a ^ b ^ c ^ d) == 0:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solve()