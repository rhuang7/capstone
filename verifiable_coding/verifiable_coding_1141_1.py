import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    first_line = input[0].split()
    T = int(first_line[0])
    M = first_line[1].decode()
    sentences = input[1:T+1]
    
    # Create a mapping from Bytelandian letters to English letters
    # Note: M is the English translation of Bytelandian "abcdefghijklmnopqrstuvwxyz"
    # So M[0] is the English letter for Bytelandian 'a', M[1] is for 'b', etc.
    # We need to create a mapping from Bytelandian letter to English letter
    # So for each i in 0-25, Bytelandian letter is chr(97 + i), English is M[i]
    # So create a dictionary: bytelandian_to_english
    bytelandian_to_english = {}
    for i in range(26):
        bytelandian_char = chr(97 + i)
        english_char = M[i]
        bytelandian_to_english[bytelandian_char] = english_char
        bytelandian_to_english[bytelandian_char.upper()] = english_char.upper()
    
    for sentence in sentences:
        translated = []
        for c in sentence:
            if c == '_':
                translated.append(' ')
            elif c in bytelandian_to_english:
                translated.append(bytelandian_to_english[c])
            else:
                # If it's a punctuation symbol, leave it as is
                translated.append(c)
        print(''.join(translated))

if __name__ == '__main__':
    solve()