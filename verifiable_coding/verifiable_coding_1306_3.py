import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        count = {}
        for c in S:
            count[c] = count.get(c, 0) + 1
        
        # Required characters for "LTIME" and "EMITL"
        required = {'L': 2, 'T': 2, 'I': 2, 'M': 1, 'E': 2}
        
        # Check if all required characters are present in sufficient quantity
        valid = True
        for char, needed in required.items():
            if count.get(char, 0) < needed:
                valid = False
                break
        
        if valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()