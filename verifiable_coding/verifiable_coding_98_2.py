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
        # Also, the total number of students is c + m + x, but we can't use more than that
        # So the answer is the minimum of (c + m) // 3 and min(c, m)
        # But also, we can't use more than the total number of students
        total_students = c + m + x
        max_teams = min((c + m) // 3, min(c, m))
        results.append(str(min(max_teams, total_students)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()