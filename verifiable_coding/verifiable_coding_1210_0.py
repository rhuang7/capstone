import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(input[idx])
        X = int(input[idx+1])
        idx += 2
        direction = input[idx]
        start_lang = input[idx+1]
        idx += 2
        if direction == 'L':
            pos = X
        else:
            pos = N - X + 1
        lang = start_lang
        for i in range(1, pos):
            if lang == 'H':
                lang = 'E'
            else:
                lang = 'H'
        P = pos
        results.append(f"{P} {lang}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()