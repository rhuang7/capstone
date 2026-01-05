import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        P1 = int(data[index])
        P2 = int(data[index+1])
        K = int(data[index+2])
        index += 3
        total_points = P1 + P2
        serve_turn = total_points // K
        if serve_turn % 2 == 0:
            results.append("CHEF")
        else:
            results.append("COOK")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()