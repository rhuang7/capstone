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
        even_A = A // 2
        odd_A = A - even_A
        even_B = B // 2
        odd_B = B - even_B
        count = even_A * even_B + odd_A * odd_B
        print(count)

if __name__ == '__main__':
    solve()