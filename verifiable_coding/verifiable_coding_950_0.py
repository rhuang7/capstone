import sys

def solve():
    N = sys.stdin.buffer.read().decode().strip()
    if not N:
        print(0)
        return

    def is_repetition_free(num):
        s = set(num)
        return len(s) == len(num) and '0' not in s

    def next_repetition_free(num):
        num = list(num)
        n = len(num)
        for i in range(n-1, -1, -1):
            if i == 0 and num[i] == '9':
                return '123456789'
            for j in range(9, int(num[i]), -1):
                if is_repetition_free(num[:i] + [str(j)] + num[i+1:]):
                    return ''.join(num[:i] + [str(j)] + num[i+1:])
        return '0'

    result = next_repetition_free(N)
    print(result)

if __name__ == '__main__':
    solve()