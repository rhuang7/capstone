import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

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
                left_4 = prefix_4[l-1]
                left_7 = prefix_7[l-1]
                right_4 = prefix_4[r] - prefix_4[l-1]
                right_7 = prefix_7[r] - prefix_7[l-1]
                if left_4 == right_7:
                    count += 1
        return count

    for s in cases:
        print(is_balanced(s))

if __name__ == '__main__':
    solve()