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
        # Check if the pairs can be connected without intersections
        # We can use a greedy approach: match A's with A's and B's with B's
        # We can count the number of A's and B's and check if they are even
        count_a = word.count('A')
        count_b = word.count('B')
        if count_a % 2 != 0 or count_b % 2 != 0:
            return False
        # Check if the word can be paired such that no two lines intersect
        # This is equivalent to checking if the word is a valid parentheses string
        # where A and B are the brackets
        # We can use a stack approach
        stack = []
        for c in word:
            if c == 'A':
                stack.append(c)
            else:
                if stack and stack[-1] == 'A':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()