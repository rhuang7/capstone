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
        Q = int(data[idx])
        idx += 1
        for __ in range(Q):
            L = int(data[idx]) - 1
            R = int(data[idx+1]) - 1
            idx += 2
            # Bitwise AND of A[L...R] is even or odd?
            # The AND is even if at least one number is even, but the AND is odd only if all numbers are odd
            # So check if there is at least one even number in the range
            even_found = False
            for i in range(L, R+1):
                if A[i] % 2 == 0:
                    even_found = True
                    break
            if even_found:
                results.append("EVEN")
            else:
                results.append("ODD")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()