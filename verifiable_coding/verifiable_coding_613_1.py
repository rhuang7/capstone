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
            if word[i] != word[i+1]:
                return False
            pairs.append((i, i+1))
        # Check if lines can be drawn without intersection
        # We need to check if the pairs can be grouped such that no two lines cross
        # This is equivalent to checking if the word is a valid parentheses string
        # with A and B as different types
        # We can use a stack approach
        stack = []
        for i in range(n):
            if word[i] == 'A':
                stack.append(i)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    count = 0
    for word in words:
        if is_bubbly(word):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()