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
        idx += 1
        board = data[idx]
        idx += 1
        points = list(map(int, data[idx:idx+8]))
        idx += 8
        
        max_score = 0
        for start in range(N - 7):
            end = start + 8
            word = board[start:end]
            letter_modifiers = []
            word_modifiers = []
            for i in range(8):
                c = word[i]
                if c == 'd':
                    letter_modifiers.append(2)
                elif c == 't':
                    letter_modifiers.append(3)
                elif c == 'D':
                    word_modifiers.append(2)
                elif c == 'T':
                    word_modifiers.append(3)
            letter_modifiers = [1 if m == 1 else m for m in letter_modifiers]
            total_letter_score = sum(p * m for p, m in zip(points, letter_modifiers))
            word_mod = 1
            for m in word_modifiers:
                word_mod *= m
            total_score = total_letter_score * word_mod
            max_score = max(max_score, total_score)
        results.append(str(max_score))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()