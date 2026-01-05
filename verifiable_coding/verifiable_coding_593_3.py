import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        prices = list(map(int, input[idx:idx+26]))
        idx += 26
        text = input[idx].decode()
        idx += 1
        present = [False] * 26
        for c in text:
            present[ord(c) - ord('a')] = True
        total = 0
        for i in range(26):
            if not present[i]:
                total += prices[i]
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()