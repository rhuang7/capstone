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
            start_pos = X
            start_lang = lang
        else:
            start_pos = N - X + 1
            start_lang = lang
        current_lang = start_lang
        current_pos = start_pos
        results.append(f"{current_pos} {current_lang}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()