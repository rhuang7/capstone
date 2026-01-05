import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    R = list(map(int, data[1:N+1]))
    
    # Create a set to keep track of people who are reported to
    reported = set()
    for i in range(N):
        if R[i] != 0:
            reported.add(R[i])
    
    # Find all people who are not in the reported set
    killers = []
    for i in range(N):
        if i + 1 not in reported:
            killers.append(i + 1)
    
    # Output the result in ascending order
    print(' '.join(map(str, killers)))

if __name__ == '__main__':
    solve()