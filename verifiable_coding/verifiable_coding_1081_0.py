import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    key = [98, 57, 31, 45, 46]
    
    for s in cases:
        encrypted = []
        for i in range(len(s)):
            msg_char = s[i]
            msg_num = ord(msg_char) - ord('A')
            key_num = key[i]
            sum_val = msg_num + key_num
            mod_val = sum_val % 26
            encrypted_char = chr(mod_val + ord('A'))
            encrypted.append(encrypted_char)
        print(''.join(encrypted))
        
if __name__ == '__main__':
    solve()