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
            
            letter_score = 0
            for i in range(8):
                letter_score += points[i] * letter_modifiers[i]
            
            word_score = letter_score
            for m in word_modifiers:
                word_score *= m
            
            max_score = max(max_score, word_score)
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()