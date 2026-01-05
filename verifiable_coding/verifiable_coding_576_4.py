import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    words = input[1:n+1]

    def count_subsequences(word):
        if 'a' not in word:
            return 0
        total = 1
        a_count = 0
        for c in word:
            if c == 'a':
                a_count += 1
            total *= (a_count + 1)
        return total - 1  # subtract 1 to exclude the empty subsequence

    for word in words:
        print(count_subsequences(word))

if __name__ == '__main__':
    solve()