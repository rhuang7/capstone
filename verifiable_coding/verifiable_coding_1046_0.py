import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        index += 2
        limak = 1
        bob = 2
        turn = 0
        while True:
            if turn % 2 == 0:
                if limak > A:
                    results.append("Bob")
                    break
                limak += bob
            else:
                if bob > B:
                    results.append("Limak")
                    break
                bob += limak
            turn += 1
    print('\n'.join(results))

if __name__ == '__main__':
    solve()