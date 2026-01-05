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
        # The maximum number of teams is limited by the minimum of:
        # 1. The sum of coders and mathematicians (since each team needs at least one of each)
        # 2. The sum of coders and mathematicians plus x (since each team needs exactly three members)
        # 3. The minimum of coders and mathematicians (since each team needs at least one of each)
        # So the maximum possible teams is the minimum of (c + m + x) // 3, min(c, m), and (c + m + x) // 3
        # But since (c + m + x) // 3 is the same as (c + m + x) // 3, we can compute it as min(c + m + x, 3 * min(c, m)) // 3
        max_teams = min(c + m + x, 3 * min(c, m)) // 3
        results.append(str(max_teams))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()