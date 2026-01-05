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
            
            total_letter_score = 0
            for i in range(8):
                letter_score = points[i]
                if letter_modifiers[i] == 2:
                    total_letter_score += letter_score * 2
                elif letter_modifiers[i] == 3:
                    total_letter_score += letter_score * 3
                else:
                    total_letter_score += letter_score
            
            word_score = total_letter_score
            for mod in word_modifiers:
                if mod == 2:
                    word_score *= 2
                elif mod == 3:
                    word_score *= 3
            
            max_score = max(max_score, word_score)
        
        results.append(max_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()