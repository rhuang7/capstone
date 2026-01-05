import sys

def solve():
    N = sys.stdin.buffer.read().decode().strip()
    if not N:
        print(0)
        return

    def is_repetition_free(num):
        s = set(num)
        return len(s) == len(num) and '0' not in s

    def next_repetition_free(num_str):
        num = list(map(int, num_str))
        n = len(num)
        for i in range(n-1, -1, -1):
            if i == 0 and num[i] == 9:
                return "123456789"
            if num[i] < 9:
                num[i] += 1
                for j in range(i+1, n):
                    num[j] = 0
                while True:
                    if is_repetition_free(num):
                        return ''.join(map(str, num))
                    for j in range(n-1, -1, -1):
                        if num[j] < 9:
                            num[j] += 1
                            for k in range(j+1, n):
                                num[k] = 0
                            break
                    else:
                        return "0"
        return "0"

    result = next_repetition_free(N)
    print(result)

if __name__ == '__main__':
    solve()