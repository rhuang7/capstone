import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_balanced(s):
        n = len(s)
        prefix_4 = [0] * (n + 1)
        prefix_7 = [0] * (n + 1)
        for i in range(n):
            prefix_4[i+1] = prefix_4[i] + (1 if s[i] == '4' else 0)
            prefix_7[i+1] = prefix_7[i] + (1 if s[i] == '7' else 0)
        count = 0
        for l in range(1, n+1):
            for r in range(l, n+1):
                total_4 = prefix_4[r] - prefix_4[l-1]
                total_7 = prefix_7[n] - prefix_7[r]
                if total_4 == total_7:
                    count += 1
        return count

    for s in cases:
        print(is_balanced(s))

if __name__ == '__main__':
    solve()