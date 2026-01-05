import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    first_line = input[0].split()
    T = int(first_line[0])
    M = first_line[1].decode()
    sentences = input[1:T+1]
    
    # Create mapping from Bytelandian to English letters
    eng_to_byt = {eng: byt for byt, eng in zip(M, "abcdefghijklmnopqrstuvwxyz")}
    byt_to_eng = {byt: eng for eng, byt in zip(M, "abcdefghijklmnopqrstuvwxyz")}
    
    for s in sentences:
        translated = []
        for c in s:
            if c == '_':
                translated.append(' ')
            elif c.isalpha():
                # Handle uppercase and lowercase
                if c.isupper():
                    translated.append(byt_to_eng[c.lower()].upper())
                else:
                    translated.append(byt_to_eng[c])
            else:
                translated.append(c)
        print(''.join(translated))
        
if __name__ == '__main__':
    solve()