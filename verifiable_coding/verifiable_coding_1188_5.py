import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    R = list(map(int, data[1:N+1]))
    
    # Create a set to track who reports to whom
    reports_to = set()
    for i in range(N):
        if R[i] != 0:
            reports_to.add(R[i])
    
    # Collect all members who are not in the reports_to set
    killers = []
    for i in range(1, N+1):
        if i not in reports_to:
            killers.append(str(i))
    
    # Output the result in ascending order
    print(' '.join(killers))

if __name__ == '__main__':
    solve()