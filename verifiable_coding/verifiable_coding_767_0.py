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
    
    # Sort citizens based on the sum of their times (to minimize the total event end time)
    citizens.sort(key=lambda x: x[0] + x[1] + x[2])
    
    # Simulate the event
    cobol_time = 0
    pole_vault_time = [0] * N
    doughnut_time = [0] * N
    
    for i in range(N):
        c, p, d = citizens[i]
        # Start COBOL after the previous person's COBOL is done
        cobol_time = max(cobol_time, i * 1)  # i is the order, 1 is the time for COBOL
        cobol_time += c
        # Start pole vault after COBOL is done
        pole_vault_time[i] = cobol_time
        pole_vault_time[i] += p
        # Start doughnut after pole vault is done
        doughnut_time[i] = pole_vault_time[i]
        doughnut_time[i] += d
    
    # The event ends when the last person finishes all tracks
    result = max(doughnut_time)
    print(result)

if __name__ == '__main__':
    solve()