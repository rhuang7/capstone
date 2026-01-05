import sys

def solve():
    key = [98, 57, 31, 45, 46]
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    for i in range(1, T + 1):
        S = data[i].decode()
        result = []
        for j in range(len(S)):
            msg_char = ord(S[j]) - ord('A')
            key_char = key[j]
            sum_val = msg_char + key_char
            mod_val = sum_val % 26
            result.append(chr(mod_val + ord('A')))
        print(''.join(result))

if __name__ == '__main__':
    solve()