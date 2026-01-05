import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        dish1 = input[idx:idx+4]
        idx += 4
        dish2 = input[idx:idx+4]
        idx += 4
        common = len(set(dish1) & set(dish2))
        if common >= 2:
            print("similar")
        else:
            print("dissimilar")

if __name__ == '__main__':
    solve()