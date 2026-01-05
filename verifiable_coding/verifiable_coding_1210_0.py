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
        lang = input[idx+1]
        idx += 2
        if direction == 'L':
            start = 1
            pos = X
        else:
            start = N
            pos = N - X + 1
        count = 1
        lang_turn = lang
        for i in range(pos - 1):
            if i % 2 == 0:
                lang_turn = 'H' if lang_turn == 'E' else 'E'
            else:
                lang_turn = 'H' if lang_turn == 'E' else 'E'
            count += 1
        results.append(f"{count} {lang_turn}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()