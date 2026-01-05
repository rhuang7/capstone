import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for case in range(1, T + 1):
        N = int(input[idx])
        idx += 1
        words = input[idx:idx + N]
        idx += N
        rhymes = {}
        for word in words:
            suffix = word[-3:]
            if suffix not in rhymes:
                rhymes[suffix] = []
            rhymes[suffix].append(word)
        print(f"Case : {case}")
        for group in rhymes.values():
            if len(group) >= 2:
                print(' '.join(group))
            else:
                for word in group:
                    print(word)

if __name__ == '__main__':
    solve()