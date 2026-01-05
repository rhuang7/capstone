import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        F1 = int(data[index])
        F2 = int(data[index+1])
        R1 = int(data[index+2])
        R2 = int(data[index+3])
        R3 = int(data[index+4])
        R4 = int(data[index+5])
        index += 6
        
        p1 = float(data[index])
        p2 = float(data[index+1])
        p3 = float(data[index+2])
        p4 = float(data[index+3])
        index += 4
        
        # Expected profit for first tournament
        expected_first = (p1 * (p2 * R1 + (1 - p2) * R2)) - F1
        
        # Expected profit for second tournament
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