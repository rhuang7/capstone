import sys

def solve():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    for i in range(1, T+1):
        hex_val = data[i]
        decimal_val = int(hex_val, 16)
        print(decimal_val)

if __name__ == '__main__':
    solve()