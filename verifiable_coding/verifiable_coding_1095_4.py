import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    perm = list(map(int, data[1:]))

    # Find the length of the longest consecutive increasing subsequence
    # starting from 1 and increasing by 1
    length = 1
    for i in range(1, N):
        if perm[i] == perm[i-1] + 1:
            length += 1
        else:
            break

    # The minimum number of moves is N - length
    print(N - length)

if __name__ == '__main__':
    solve()