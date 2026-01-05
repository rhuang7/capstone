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
        # Check if the word can be paired such that no lines intersect
        # We can use a greedy approach: pair A's with A's and B's with B's
        # and check if the pairs can be arranged without overlapping
        # We can simulate the pairing by checking the order of the letters
        # and ensuring that same letters are paired in the same order
        # We can use a stack-based approach
        stack = []
        for i in range(n):
            if word[i] == 'A':
                stack.append(i)
            else:
                if stack:
                    # Pair the last A with this B
                    # Check if this B is in the correct position
                    # If the last A is before this B, it's okay
                    # If the last A is after this B, it's not okay
                    if stack[-1] < i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()