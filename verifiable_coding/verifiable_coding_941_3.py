import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        even_x = A // 2
        odd_x = A - even_x
        even_y = B // 2
        odd_y = B - even_y
        count = even_x * even_y + odd_x * odd_y
        print(count)

if __name__ == '__main__':
    solve()