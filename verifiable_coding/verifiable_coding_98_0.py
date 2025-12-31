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
        # But also, the total number of students is c + m + x, and each team needs 3 students
        total_students = c + m + x
        max_teams_by_students = total_students // 3
        # The maximum number of teams is also limited by the minimum of c and m
        max_teams_by_specializations = min(c, m)
        # The actual maximum is the minimum of the two
        result = min(max_teams_by_students, max_teams_by_specializations)
        results.append(str(result))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()