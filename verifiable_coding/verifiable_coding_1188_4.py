import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    R = list(map(int, data[1:N+1]))
    
    # Create a set to store the indices of potential killers
    killers = set()
    
    # Create a set to store all reported members
    reported = set()
    
    for i in range(N):
        if R[i] == 0:
            # This is the Don, he reports to nobody
            continue
        reported.add(R[i])
    
    # All members not in reported are potential killers
    for i in range(1, N+1):
        if i not in reported:
            killers.add(i)
    
    # Convert to sorted list and print
    print(' '.join(map(str, sorted(killers))))

if __name__ == '__main__':
    solve()