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
        # We can count the number of A's and B's and check if they are even
        count_a = word.count('A')
        count_b = word.count('B')
        if count_a % 2 != 0 or count_b % 2 != 0:
            return False
        # Check if the word can be paired such that no two lines intersect
        # We can simulate the pairing process
        a_pos = []
        b_pos = []
        for i, c in enumerate(word):
            if c == 'A':
                a_pos.append(i)
            else:
                b_pos.append(i)
        # Pair A's and B's in order
        # If the positions of A's and B's are interleaved, it's not bubbly
        # For example, ABAB is not bubbly
        # Check if the A positions and B positions are non-interleaving
        i = j = 0
        while i < len(a_pos) and j < len(b_pos):
            if a_pos[i] < b_pos[j]:
                i += 1
            else:
                j += 1
        return i == len(a_pos) and j == len(b_pos)

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()