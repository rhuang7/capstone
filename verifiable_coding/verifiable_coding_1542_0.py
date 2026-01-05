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
            
            for i in range(8):
                modifier = letters[i]
                if modifier == 'd':
                    letter_modifiers.append(2)
                elif modifier == 't':
                    letter_modifiers.append(3)
                elif modifier == 'D':
                    word_modifiers.append(2)
                elif modifier == 'T':
                    word_modifiers.append(3)
            
            word_mod = 1
            for m in word_modifiers:
                word_mod *= m
            
            total = 0
            for i in range(8):
                p = points[i]
                m = 1
                if letters[i] in ['d', 't']:
                    m = letter_modifiers[i]
                total += p * m
            
            total *= word_mod
            if total > max_score:
                max_score = total
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()