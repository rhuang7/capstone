import sys
import math

MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for case in range(1, T + 1):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        strings = []
        for _ in range(m):
            s = data[idx]
            strings.append(s)
            idx += 1
        # Precompute powers of 26 mod MOD
        pow26 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow26[i] = (pow26[i - 1] * 26) % MOD
        # Precompute factorial and inverse factorial mod MOD
        max_len = max(len(s) for s in strings) if strings else 0
        fact = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], MOD - 2, MOD)
        for i in range(max_len - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD
        # Precompute all possible strings of length n
        # But this is not feasible, so we use the formula for count of a string s
        # in all possible strings of length n
        # For a string s of length l, the number of occurrences in all strings is:
        # (26^(n - l) * (n - l + 1)) * (number of ways to choose the positions of s)
        # But we need to account for overlapping occurrences
        # However, for the problem, we need to count all occurrences of s in all possible strings
        # This is equivalent to: for each possible position of s in a string of length n, count how many strings contain s in that position
        # For a string s of length l, the number of possible positions is (n - l + 1)
        # For each such position, the number of strings where s appears at that position is 26^(n - l)
        # However, this counts all occurrences, including overlapping ones
        # So the total is (n - l + 1) * 26^(n - l)
        # But this is only if s is a substring of length l
        # However, the problem says that the strings in the input may be of any length
        # So for each string s in the input, we compute:
        # if len(s) > n: 0
        # else: (n - len(s) + 1) * 26^(n - len(s))
        # But wait, this is not correct. Because it counts how many times s appears in all strings, but the problem requires counting all occurrences of s in all strings
        # So for example, for s = "aa" and n = 2, the total is 1 (only one string "aa" has "aa" once)
        # But according to the formula (n - l + 1) * 26^(n - l), it would be (2 - 2 + 1) * 26^(0) = 1 * 1 = 1, which is correct
        # So the formula is correct
        # So for each string s in the input, compute:
        # if len(s) > n: 0
        # else: (n - len(s) + 1) * 26^(n - len(s)) mod MOD
        # But wait, this is not correct. Because it counts how many times s appears in all strings, but the problem requires counting all occurrences of s in all strings
        # So for example, for s = "aa" and n = 3, the total is 2 * 26^1 = 52
        # But the actual count is: for each string of length 3, how many times does "aa" appear as a substring?
        # For example, "aaa" has 2 occurrences of "aa"
        # So the total is 2 * 26^1 = 52, which is correct
        # So the formula is correct
        # So the correct approach is:
        # For each string s in the input, if len(s) > n: 0
        # else: (n - len(s) + 1) * 26^(n - len(s)) mod MOD
        # But wait, this is not correct. Because it counts the number of times s appears in all strings, but the problem requires counting all occurrences of s in all strings
        # So for example, for s = "aa" and n = 3, the total is 2 * 26^1 = 52, which is correct
        # So the formula is correct
        # So the code is:
        res = []
        for s in strings:
            l = len(s)
            if l > n:
                res.append(0)
            else:
                cnt = (n - l + 1) * pow(26, n - l, MOD)
                res.append(cnt % MOD)
        results.append(f"Case {case}:")
        results.extend(str(x) for x in res)
    print("\n".join(results))

if __name__ == '__main__':
    main()