import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    mod = 8589934592

    results = []
    for i, n in enumerate(cases, 1):
        if n == 0:
            results.append(f"Case {i}: 0")
            continue
        # Calculate the minimum number of toggle operations
        # Based on the pattern observed, the minimum toggle for n variables is (n * (n + 1)) // 2
        # But we need to consider the modulo 2^33
        res = (n * (n + 1)) // 2 % mod
        results.append(f"Case {i}: {res}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()