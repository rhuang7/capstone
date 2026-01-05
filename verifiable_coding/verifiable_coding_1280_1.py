import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        s = data[i]
        n = len(s)
        operations = 0
        for j in range(n // 2):
            left = s[j]
            right = s[n - 1 - j]
            if left != right:
                # Find the minimum steps to make left and right equal
                # We can only decrease characters, so we need to find the lowest common character
                # that both can be reduced to
                # The lowest common character is the minimum of the two characters
                # So we find the minimum between left and right
                min_char = min(left, right)
                # The number of operations is the sum of the steps to reduce both to min_char
                operations += (ord(left) - ord(min_char)) + (ord(right) - ord(min_char))
        results.append(str(operations))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()