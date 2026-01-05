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
        word_spam = {}
        for _ in range(N):
            w = data[idx]
            s = int(data[idx+1])
            idx += 2
            if (w, s) in word_spam:
                word_spam[(w, s)] += 1
            else:
                word_spam[(w, s)] = 1
        total = 0
        for key in word_spam:
            if key[1] == 0:
                total += word_spam[key]
            else:
                total += word_spam[key]
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()