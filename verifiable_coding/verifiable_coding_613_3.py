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
        # Sort pairs based on the first character
        pairs.sort(key=lambda x: word[x[0]])
        # Check if any two pairs overlap
        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                a, b = pairs[i]
                c, d = pairs[j]
                if (a < c < b < d) or (c < a < d < b):
                    return False
        return True

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()