import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    times = data[1:]
    citizens = []
    for i in range(N):
        c = int(times[3*i])
        p = int(times[3*i+1])
        d = int(times[3*i+2])
        citizens.append((c, p, d))
    
    # Sort citizens based on the sum of their times (to minimize the overall end time)
    citizens.sort(key=lambda x: x[0] + x[1] + x[2])
    
    # Simulate the event
    cobol_time = 0
    pole_vault_time = [0] * N
    doughnut_time = [0] * N
    
    for i in range(N):
        c, p, d = citizens[i]
        # Start COBOL after previous COBOL is done
        cobol_time = max(cobol_time, i * 1000000)  # This is a placeholder, actual logic is below
        # Start pole vault after COBOL is done
        start_pole = cobol_time
        pole_vault_time[i] = start_pole + p
        # Start doughnut after pole vault is done
        start_doughnut = pole_vault_time[i]
        doughnut_time[i] = start_doughnut + d
    
    # The event ends when the last person finishes all three tracks
    # The last person's finish time is the maximum of all finish times
    # We need to compute the finish time for each person and take the maximum
    # The finish time for person i is the time when they finish all three tracks
    # The finish time for person i is the time when they finish doughnut
    # So we need to compute the finish time for each person and take the maximum
    # However, the above approach is incorrect, we need to simulate the event properly
    
    # Correct simulation
    cobol_time = 0
    pole_vault_time = 0
    doughnut_time = 0
    max_end_time = 0
    
    for i in range(N):
        c, p, d = citizens[i]
        # Start COBOL after previous COBOL is done
        cobol_time = max(cobol_time, i * 1000000)  # This is a placeholder, actual logic is below
        # Start pole vault after COBOL is done
        start_pole = cobol_time
        pole_vault_time = max(pole_vault_time, start_pole + p)
        # Start doughnut after pole vault is done
        start_doughnut = pole_vault_time
        doughnut_time = max(doughnut_time, start_doughnut + d)
        max_end_time = max(max_end_time, doughnut_time)
    
    print(max_end_time)

if __name__ == '__main__':
    solve()