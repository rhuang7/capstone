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
        a_positions = [i for i, c in enumerate(word) if c == 'A']
        b_positions = [i for i, c in enumerate(word) if c == 'B']
        if len(a_positions) % 2 != 0 or len(b_positions) % 2 != 0:
            return False
        a_pairs = []
        b_pairs = []
        i = 0
        j = 0
        while i < len(a_positions) and j < len(b_positions):
            a_pairs.append((a_positions[i], a_positions[i+1]))
            b_pairs.append((b_positions[j], b_positions[j+1]))
            i += 2
            j += 2
        for a1, a2 in a_pairs:
            for b1, b2 in b_pairs:
                if (a1 < b1 and a2 > b2) or (a1 > b1 and a2 < b2):
                    return False
        return True

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()