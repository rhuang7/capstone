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
                modifier = word[i]
                if modifier == 'd':
                    letter_modifiers.append(2)
                elif modifier == 't':
                    letter_modifiers.append(3)
                elif modifier == 'D':
                    word_modifiers.append(2)
                elif modifier == 'T':
                    word_modifiers.append(3)
            
            # Apply letter modifiers
            total = 0
            for i in range(8):
                letter_score = points[i]
                if letter_modifiers[i] == 2:
                    total += letter_score * 2
                elif letter_modifiers[i] == 3:
                    total += letter_score * 3
                else:
                    total += letter_score
            
            # Apply word modifiers
            if word_modifiers:
                if 2 in word_modifiers:
                    total *= 2
                if 3 in word_modifiers:
                    total *= 3
            
            max_score = max(max_score, total)
        
        results.append(str(max_score))
    
    print('\n'.join(results))