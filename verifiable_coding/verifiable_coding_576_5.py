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
                for j in range(i+1, m):
                    count += 1
        print(count)

if __name__ == '__main__':
    solve()