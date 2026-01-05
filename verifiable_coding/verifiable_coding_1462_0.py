import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    for i in range(1, T+1):
        s = input[i].decode().lower()
        berhampore = 'berhampore' in s
        serampore = 'serampore' in s
        if berhampore and serampore:
            print("Both")
        elif berhampore:
            print("GCETTB")
        elif serampore:
            print("GCETTS")
        else:
            print("Others")

if __name__ == '__main__':
    solve()