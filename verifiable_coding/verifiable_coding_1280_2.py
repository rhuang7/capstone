import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        operations = 0
        for j in range(n // 2):
            left = S[j]
            right = S[n - 1 - j]
            if left != right:
                # Find the minimum steps to make left and right equal
                # We can only decrease characters, so we need to find the minimum steps to make both equal to some common character
                # The optimal is to make both equal to the lower of the two
                if left < right:
                    target = left
                    operations += (right - target)
                else:
                    target = right
                    operations += (left - target)
        results.append(str(operations))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()