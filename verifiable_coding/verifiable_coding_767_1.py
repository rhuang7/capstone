import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    times = data[1:]
    
    # Extract COBOL, pole vault, doughnut-eating times
    cobol = []
    pole = []
    dough = []
    for i in range(N):
        cobol.append(int(times[3*i]))
        pole.append(int(times[3*i+1]))
        dough.append(int(times[3*i+2]))
    
    # Sort the citizens based on the sum of their times
    # This is a heuristic to minimize the overall event end time
    citizens = sorted(zip(cobol, pole, dough), key=lambda x: x[0] + x[1] + x[2])
    
    # Simulate the event
    # Track the current time and the time when the next person can start COBOL
    current_time = 0
    cobol_time = 0
    pole_time = 0
    dough_time = 0
    
    for i in range(N):
        cobol_time = max(cobol_time, current_time) + citizens[i][0]
        pole_time = cobol_time + citizens[i][1]
        dough_time = pole_time + citizens[i][2]
        current_time = max(current_time, dough_time)
    
    print(current_time)

if __name__ == '__main__':
    solve()