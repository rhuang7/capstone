import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx += 2
        min_entry = A + B
        max_entry = A + B
        if A == 0 and B == 0:
            print("0 0")
            continue
        if A == 0:
            min_entry = B
            max_entry = B
        elif B == 0:
            min_entry = A
            max_entry = A
        else:
            min_entry = A + B
            max_entry = A + B
        print(f"{min_entry} {max_entry}")

if __name__ == '__main__':
    solve()