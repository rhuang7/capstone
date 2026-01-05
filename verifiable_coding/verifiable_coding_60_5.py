import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        # The minimal value is (a ^ x) + (b ^ x)
        # Let's find the minimal value by considering the binary bits
        # The minimal value is (a ^ b) because (a ^ x) + (b ^ x) = a ^ b + 2*(x & (a ^ b))
        # So the minimal value is when x & (a ^ b) = 0, which gives (a ^ b)
        results.append(str(a ^ b))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()