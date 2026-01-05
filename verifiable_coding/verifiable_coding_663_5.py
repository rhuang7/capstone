import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        L = int(data[index])
        S = data[index + 1]
        index += 2
        n = len(S)
        # The lex smallest string is the smallest rotation of the first L characters
        # We can generate all possible rotations of the first L characters and find the smallest
        min_str = S
        for i in range(L):
            rotated = S[i:] + S[:i]
            if rotated < min_str:
                min_str = rotated
        results.append(min_str)
    print('\n'.join(results))

if __name__ == '__main__':
    solve()