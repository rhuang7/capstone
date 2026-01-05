import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    words = data[1:M+1]

    def is_bubbly(word):
        n = len(word)
        if n % 2 != 0:
            return False
        pairs = []
        for i in range(0, n, 2):
            pairs.append((i, i+1))
        # Check if the word can be paired such that no two lines intersect
        # We can use a greedy approach: pair A's with A's and B's with B's
        # If the word has equal number of A's and B's, then it's bubbly
        # But this is not sufficient, we need to check the order
        # A valid bubbly word must have the same number of A's and B's and the sequence must be such that A's and B's alternate
        # So the word must be of the form ABABAB... or BABA...B
        # So check if the word is alternating
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                return False
        return True

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()