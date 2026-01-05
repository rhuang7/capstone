import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    words = input[1:n+1]

    def count_subsequences(word):
        if 'a' not in word:
            return 0
        count = 1
        a_count = 0
        for c in word:
            if c == 'a':
                a_count += 1
            else:
                count *= 2
        return count * (2 ** (a_count - 1))

    for word in words:
        print(count_subsequences(word))

if __name__ == '__main__':
    solve()