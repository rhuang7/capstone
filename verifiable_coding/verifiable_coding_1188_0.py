import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    R = list(map(int, data[1:N+1]))
    
    # Create a set to store the indices of potential killers
    killers = set()
    
    # Create a frequency dictionary to count how many people report to each member
    report_count = {}
    
    for i in range(N):
        if R[i] != 0:
            report_count[R[i]] = report_count.get(R[i], 0) + 1
    
    # Check which members are not reported by anyone
    for i in range(N):
        if R[i] != 0:
            continue
        if i + 1 not in report_count:
            killers.add(i + 1)
    
    # Convert the set to a sorted list and print as space-separated string
    print(' '.join(map(str, sorted(killers))))

if __name__ == '__main__':
    solve()