import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    for i in range(1, T+1):
        s = input[i].decode().lower()
        has_berhampore = 'berhampore' in s
        has_serampore = 'serampore' in s
        if has_berhampore and has_serampore:
            print("Both")
        elif has_berhampore:
            print("GCETTB")
        elif has_serampore:
            print("GCETTS")
        else:
            print("Others")

if __name__ == '__main__':
    solve()