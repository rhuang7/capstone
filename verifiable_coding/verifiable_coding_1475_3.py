import sys

def solve():
    import sys
    from collections import defaultdict

    data = sys.stdin.buffer.read().split()
    S = data[0]
    K = data[1]

    l = len(S)
    k = len(K)

    positions = []

    for i in range(l - k + 1):
        substring = S[i:i+k]
        sorted_sub = ''.join(sorted(substring))
        positions.append(str(i + 1))

    result = 'The antidote is found in ' + ''.join(positions) + '.'
    print(result)

if __name__ == '__main__':
    solve()