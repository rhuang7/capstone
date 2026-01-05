import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    words = input[1:n+1]

    for word in words:
        count = 0
        m = len(word)
        for i in range(m):
            if word[i] == 'a':
                count += 1
        if count == 0:
            print(0)
        else:
            print(2 ** m - 1)

if __name__ == '__main__':
    solve()