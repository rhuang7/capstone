import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        X = int(data[idx+1])
        idx += 2
        direction = data[idx]
        lang = data[idx+1]
        idx += 2
        if direction == 'L':
            start_pos = X
        else:
            start_pos = N - X + 1
        turn = 0
        current_lang = lang
        for i in range(start_pos - 1):
            turn += 1
            if turn % 2 == 1:
                current_lang = 'H' if current_lang == 'E' else 'E'
            else:
                current_lang = 'E' if current_lang == 'H' else 'H'
        P = start_pos
        results.append(f"{P} {current_lang}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()