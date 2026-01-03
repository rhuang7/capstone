import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        S1 = input[idx]
        idx += 1
        S2 = input[idx]
        idx += 1
        len1 = len(S1)
        len2 = len(S2)
        min_ugliness = float('inf')
        for i in range(len1):
            for j in range(len2):
                if S1[i] == S2[j]:
                    l1 = len1 - i
                    l2 = len2 - j
                    petal_lengths = [l1, l2]
                    ugliness = abs(l1 - l2) + abs(l2 - l1) + abs(l1 - l2) + abs(l2 - l1)
                    min_ugliness = min(min_ugliness, ugliness)
        print(min_ugliness)

if __name__ == '__main__':
    solve()