import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    R = list(map(int, data[1:N+1]))
    
    # Create a set to track who reports to whom
    reporters = set()
    for i in range(N):
        if R[i] != 0:
            reporters.add(R[i])
    
    # Collect all members not in the reporters set
    killers = []
    for i in range(1, N+1):
        if i not in reporters:
            killers.append(i)
    
    # Output the result in ascending order
    print(' '.join(map(str, killers)))

if __name__ == '__main__':
    solve()