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
        even_a = A // 2
        odd_a = A - even_a
        even_b = B // 2
        odd_b = B - even_b
        count = even_a * even_b + odd_a * odd_b
        print(count)

if __name__ == '__main__':
    solve()