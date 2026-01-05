import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    mod = 8589934592

    result = []
    for i, n in enumerate(cases, 1):
        if n == 0:
            result.append(f"Case {i}: 0")
        else:
            # The minimum number of toggle is the number of bits in the Gray code sequence of length n
            # The number of toggles is equal to the number of bits in the Gray code sequence of length n
            # The number of bits in the Gray code sequence of length n is 2^n
            # But we need to find the minimum number of toggles for all 2^n combinations
            # The minimum number of toggles is the number of bits in the Gray code sequence of length n
            # Which is 2^n
            # However, for large n, we need to compute 2^n mod 2^33
            # Since 2^33 is 8589934592
            # So we compute (2^n) % mod
            # But since n can be up to 1020, we need to compute 2^n mod mod efficiently
            # Using fast exponentiation
            def pow_mod(a, b, mod):
                result = 1
                a = a % mod
                while b > 0:
                    if b % 2 == 1:
                        result = (result * a) % mod
                    a = (a * a) % mod
                    b = b // 2
                return result

            ans = pow_mod(2, n, mod)
            result.append(f"Case {i}: {ans}")
    print('\n'.join(result))

if __name__ == '__main__':
    solve()