import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    first_line = input[0]
    T_str, M = first_line.decode().split()
    T = int(T_str)
    M = M
    # Create a mapping from Bytelandian letters to English letters
    eng_to_byt = {chr(ord('a') + i): M[i] for i in range(26)}
    byt_to_eng = {M[i]: chr(ord('a') + i) for i in range(26)}
    # Process each sentence
    for line in input[1:T+1]:
        line = line.decode()
        translated = []
        for c in line:
            if c == '_':
                translated.append(' ')
            elif c.isalpha():
                # Check if it's uppercase
                if c.isupper():
                    translated.append(byt_to_eng[c.lower()].upper())
                else:
                    translated.append(byt_to_eng[c])
            else:
                translated.append(c)
        print(''.join(translated))

if __name__ == '__main__':
    solve()