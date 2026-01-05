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
            letters = board[start:end]
            letter_modifiers = []
            word_modifiers = []
            for c in letters:
                if c == 'd':
                    letter_modifiers.append(2)
                elif c == 't':
                    letter_modifiers.append(3)
                elif c == 'D':
                    word_modifiers.append(2)
                elif c == 'T':
                    word_modifiers.append(3)
            letter_modifiers = [1 if m == 1 else m for m in letter_modifiers]
            word_modifiers = [1 if m == 1 else m for m in word_modifiers]
            word_mod = 1
            for m in word_modifiers:
                word_mod *= m
            letter_score = 0
            for i in range(8):
                letter = letters[i]
                if letter in ['d', 't']:
                    letter_score += points[i] * letter_modifiers[i]
                else:
                    letter_score += points[i]
            total_score = letter_score * word_mod
            if total_score > max_score:
                max_score = total_score
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()