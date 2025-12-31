import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:]))

    total_xor = 0
    for num in a:
        total_xor ^= num

    result = []
    for num in a:
        result.append(total_xor ^ num)
    
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()