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
        current_lang = lang
        for i in range(pos-1):
            if i % 2 == 0:
                current_lang = 'H' if current_lang == 'E' else 'E'
            else:
                current_lang = 'H' if current_lang == 'E' else 'E'
            count += 1
        results.append(f"{count} {current_lang}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()