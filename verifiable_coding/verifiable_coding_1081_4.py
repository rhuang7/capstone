import sys

def solve():
    key = [98, 57, 31, 45, 46]
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    for i in range(1, T + 1):
        S = data[i].decode()
        result = []
        for j in range(len(S)):
            msg_num = ord(S[j]) - ord('A')
            key_num = key[j]
            total = msg_num + key_num
            mod = total % 26
            result.append(chr(mod + ord('A')))
        print(''.join(result))

if __name__ == '__main__':
    solve()