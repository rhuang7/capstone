import sys

def solve():
    key = [98, 57, 31, 45, 46]
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    for i in range(1, T + 1):
        S = data[i].decode()
        encrypted = ""
        for j in range(len(S)):
            original = ord(S[j]) - ord('A')
            sum_val = original + key[j]
            encrypted += chr((sum_val % 26) + ord('A'))
        print(encrypted)

if __name__ == '__main__':
    solve()