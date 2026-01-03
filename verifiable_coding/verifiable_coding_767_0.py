import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    times = []
    idx = 1
    for _ in range(N):
        cobol = int(data[idx])
        pole = int(data[idx+1])
        dough = int(data[idx+2])
        times.append((cobol, pole, dough))
        idx += 3
    
    # Sort the citizens based on the sum of their times (to minimize the total event end time)
    times.sort(key=lambda x: x[0] + x[1] + x[2])
    
    # Simulate the event
    cobol_time = 0
    pole_time = [0] * N
    dough_time = [0] * N
    
    for i in range(N):
        cobol, pole, dough = times[i]
        # Start COBOL after previous COBOL is done
        cobol_time += cobol
        # Start pole vault after COBOL is done
        pole_time[i] = cobol_time
        # Start doughnut-eating after pole vault is done
        dough_time[i] = pole_time[i] + pole
        # Update the maximum time
        max_time = max(max_time, dough_time[i])
    
    print(max_time)

if __name__ == '__main__':
    solve()