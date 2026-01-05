import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        M = int(data[idx])
        N = int(data[idx+1])
        idx += 2
        count_pairs = 0
        count_x = 0
        for x in range(1, M+1):
            for y in range(1, N+1):
                product = x * y
                sum_val = x + y
                if str(product + sum_val) == str(x) + str(y):
                    count_pairs += 1
                    count_x += 1
        results.append(f"{count_pairs} {count_x}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()