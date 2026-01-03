import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    A.sort(reverse=True)

    for i in range(N - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            # Check for lex largest triplet
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if A[i] < A[j] + A[k]:
                        print("YES")
                        print(A[i], A[j], A[k])
                        return
    print("NO")

if __name__ == '__main__':
    solve()