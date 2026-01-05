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

    # Sort the citizens based on the sum of their times (COBOL + Pole vault + Doughnut-eating)
    # This is a heuristic that works for this problem
    times.sort(key=lambda x: x[0] + x[1] + x[2])

    # Simulate the event
    # Track the current time and the current time when the computer is free
    current_time = 0
    computer_free = 0

    for c, p, d in times:
        # Wait until the computer is free
        if current_time < computer_free:
            current_time = computer_free
        # Start COBOL programming
        current_time += c
        # Computer is now free after this
        computer_free = current_time
        # Start pole vault immediately
        current_time += p
        # Start doughnut-eating immediately
        current_time += d

    print(current_time)

if __name__ == '__main__':
    solve()