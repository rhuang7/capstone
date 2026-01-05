import sys

def solve():
    import sys
    N = sys.stdin.buffer.read().decode().strip()
    if not N:
        print(0)
        return

    def is_repetition_free(s):
        return len(set(s)) == len(s) and '0' not in s

    def next_repetition_free(n_str):
        n = int(n_str)
        for i in range(n + 1, 10**9):
            s = str(i)
            if is_repetition_free(s):
                return s
        return "0"

    result = next_repetition_free(N)
    print(result)

if __name__ == '__main__':
    solve()