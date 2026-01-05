import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().splitlines()
    first_line = input[0].decode().split()
    T = int(first_line[0])
    M = first_line[1]
    bytelandian_to_english = {}
    for i in range(26):
        bytelandian_to_english[ord(M[i]) - ord('a')] = chr(ord('a') + i)
    for i in range(26):
        bytelandian_to_english[ord(M[i]) - ord('A')] = chr(ord('A') + i)
    for line in input[1:T+1]:
        translated = []
        for c in line:
            if c == '_':
                translated.append(' ')
            elif c in bytelandian_to_english:
                translated.append(chr(bytelandian_to_english[ord(c) - ord('a')] + (ord(c) - ord('a')) % 26))
            else:
                translated.append(c)
        print(''.join(translated))

if __name__ == '__main__':
    solve()