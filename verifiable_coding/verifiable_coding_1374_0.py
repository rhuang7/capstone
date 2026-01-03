import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        F1 = int(data[idx])
        F2 = int(data[idx+1])
        R1 = int(data[idx+2])
        R2 = int(data[idx+3])
        R3 = int(data[idx+4])
        R4 = int(data[idx+5])
        idx += 6
        
        p1 = float(data[idx])
        p2 = float(data[idx+1])
        p3 = float(data[idx+2])
        p4 = float(data[idx+3])
        idx += 4
        
        # Calculate expected profit for first tournament
        expected_first = (p1 * (p2 * R1 + (1 - p2) * R2)) - F1
        
        # Calculate expected profit for second tournament
        expected_second = (p3 * (p4 * R3 + (1 - p4) * R4)) - F2
        
        if expected_first > expected_second:
            results.append("FIRST")
        elif expected_first < expected_second:
            results.append("SECOND")
        else:
            results.append("BOTH")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()