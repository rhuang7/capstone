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
    # So M[0] is the English letter for Bytelandian 'a', M[1] for 'b', etc.
    # So we need to create a reverse mapping: for each English letter, find its Bytelandian counterpart
    # But since M is the English translation of Bytelandian letters, we need to map Bytelandian letters to English letters
    # So for Bytelandian 'a', English is M[0], so we create a dictionary where key is Bytelandian letter, value is English letter
    # But since M is a permutation of the English alphabet, we can create a dictionary where for each English letter, we find its Bytelandian counterpart
    # So we need to create a mapping from Bytelandian letters to English letters
    # So for Bytelandian 'a', English is M[0], so we create a dictionary: bytelandian_to_english = { 'a': M[0], 'b': M[1], ... }
    # Then, for each character in the sentence, if it is a lowercase letter, we replace it with bytelandian_to_english[character]
    # If it is an uppercase letter, we replace it with the uppercase version of the corresponding English letter
    # If it is an underscore, replace with space
    # If it is a punctuation symbol, leave it as is
    
    # Create the mapping
    bytelandian_to_english = {}
    for i in range(26):
        bytelandian_to_english[chr(ord('a') + i)] = M[i]
    
    # Process each sentence
    for sentence in sentences:
        translated = []
        for c in sentence:
            if c == '_':
                translated.append(' ')
            elif c.isalpha():
                # Check if it's uppercase
                is_upper = c.isupper()
                # Get the lowercase version
                lower_c = c.lower()
                # Get the corresponding English letter
                eng_char = bytelandian_to_english[lower_c]
                # If it was uppercase, make it uppercase
                if is_upper:
                    translated.append(eng_char.upper())
                else:
                    translated.append(eng_char)
            else:
                # It's a punctuation symbol, leave it as is
                translated.append(c)
        print(''.join(translated))
    
if __name__ == '__main__':
    solve()