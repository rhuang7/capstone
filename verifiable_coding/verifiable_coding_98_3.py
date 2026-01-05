import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    q = int(data[0])
    index = 1
    results = []
    for _ in range(q):
        c = int(data[index])
        m = int(data[index+1])
        x = int(data[index+2])
        index += 3
        # The maximum number of teams is limited by the minimum of (c + m) // 3 and the minimum of c and m
        # Also, the number of teams cannot exceed the sum of coders and mathematicians
        max_teams = min((c + m) // 3, min(c, m))
        results.append(str(max_teams))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()