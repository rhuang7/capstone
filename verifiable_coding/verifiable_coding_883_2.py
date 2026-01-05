import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        counts = list(map(int, data[idx:idx+N]))
        idx += N
        # Calculate the total number of passes
        total_pass = sum(counts)
        # Check if the total passes is consistent with the counts
        # If a student passed, they see total_pass - 1 passes
        # If a student failed, they see total_pass passes
        # So, for each count, it must be either total_pass or total_pass - 1
        valid = True
        for c in counts:
            if c not in (total_pass, total_pass - 1):
                valid = False
                break
        if not valid:
            results.append("-1")
            continue
        # Now check if the number of students who saw total_pass - 1 is equal to the number of passes
        # Because if a student passed, they see total_pass - 1 passes
        # So the number of passes is equal to the number of students who saw total_pass - 1
        num_pass = counts.count(total_pass - 1)
        if num_pass != total_pass:
            results.append("-1")
        else:
            results.append(str(N - total_pass))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()