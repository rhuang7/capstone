import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if (A[i] ^ A[j] ^ A[k] ^ A[l]) == 0:
                        print("Yes")
                        return
    print("No")

if __name__ == '__main__':
    solve()