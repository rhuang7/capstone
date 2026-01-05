import sys

def solve():
    import sys
    from collections import defaultdict

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    data = sys.stdin.buffer.read().split()
    S = ' '.join(data[:-1])
    K = data[-1]

    l = len(S)
    k = len(K)

    positions = []

    for i in range(l - k + 1):
        substring = S[i:i+k]
        if is_anagram(substring, K):
            positions.append(str(i + 1))  # positions are 1-based

    print("The antidote is found in " + ''.join(positions) + ".")

if __name__ == '__main__':
    solve()