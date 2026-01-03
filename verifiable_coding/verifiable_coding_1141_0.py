import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    first_line = input[0].split()
    T = int(first_line[0])
    M = first_line[1].decode()
    sentences = input[1:T+1]
    
    # Create a mapping from Bytelandian letters to English letters
    eng_to_byt = {chr(ord('a') + i): M[i] for i in range(26)}
    byt_to_eng = {v: k for k, v in eng_to_byt.items()}
    
    for s in sentences:
        translated = []
        for c in s.decode():
            if c == '_':
                translated.append(' ')
            elif c.isalpha():
                # Preserve case
                if c.isupper():
                    translated.append(byt_to_eng[c.lower()].upper())
                else:
                    translated.append(byt_to_eng[c])
            else:
                translated.append(c)
        print(''.join(translated))
        
if __name__ == '__main__':
    solve()