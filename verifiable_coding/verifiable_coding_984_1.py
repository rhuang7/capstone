import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        even_count = 0
        total = 0
        for num in A:
            if num % 2 == 0:
                even_count += 1
            else:
                total += even_count
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()