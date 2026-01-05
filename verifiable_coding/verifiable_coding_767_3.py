import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    times = []
    idx = 1
    for _ in range(N):
        c = int(data[idx])
        p = int(data[idx+1])
        d = int(data[idx+2])
        times.append((c, p, d))
        idx += 3

    # Sort the citizens based on the sum of their times (COBOL + pole vault + doughnut-eating)
    # This is a greedy approach to minimize the total end time
    times.sort(key=lambda x: x[0] + x[1] + x[2])

    # Simulate the event
    cobol_time = 0
    pole_vault_time = 0
    doughnut_time = 0

    for c, p, d in times:
        # COBOL is a single resource, so we have to wait for it to be free
        cobol_time += c
        # Once COBOL is done, the person moves to pole vault
        pole_vault_time = max(pole_vault_time, cobol_time) + p
        # Once pole vault is done, the person moves to doughnut-eating
        doughnut_time = max(doughnut_time, pole_vault_time) + d

    print(max(cobol_time, pole_vault_time, doughnut_time))

if __name__ == '__main__':
    solve()