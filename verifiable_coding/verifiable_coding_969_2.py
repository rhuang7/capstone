import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split('\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        while idx < len(data) and data[idx] == '':
            idx += 1
        if idx >= len(data):
            break
        activities, origin = data[idx].split()
        activities = int(activities)
        idx += 1
        laddus = 0
        for _ in range(activities):
            while idx < len(data) and data[idx] == '':
                idx += 1
            if idx >= len(data):
                break
            activity = data[idx].split()
            idx += 1
            if activity[0] == 'CONTEST_WON':
                rank = int(activity[1])
                laddus += 300 + max(0, 20 - rank)
            elif activity[0] == 'TOP_CONTRIBUTOR':
                laddus += 300
            elif activity[0] == 'BUG_FOUND':
                severity = int(activity[1])
                laddus += severity
            elif activity[0] == 'CONTEST_HOSTED':
                laddus += 50
        min_redeem = 200 if origin == 'INDIAN' else 400
        results.append(str(laddus // min_redeem))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()