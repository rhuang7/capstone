import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    # Check for any four consecutive elements
    for i in range(n - 3):
        a = A[i]
        b = A[i+1]
        c = A[i+2]
        d = A[i+3]
        if (a ^ b ^ c ^ d) == 0:
            print("Yes")
            return

    # Check for any four elements with two pairs of consecutive elements
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            a = A[i]
            b = A[i+1]
            c = A[j]
            d = A[j+1]
            if (a ^ b ^ c ^ d) == 0:
                print("Yes")
                return

    # Check for any four elements with two pairs of non-consecutive elements
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n - 1):
                a = A[i]
                b = A[j]
                c = A[k]
                d = A[n-1]
                if (a ^ b ^ c ^ d) == 0:
                    print("Yes")
                    return

    print("No")

if __name__ == '__main__':
    solve()