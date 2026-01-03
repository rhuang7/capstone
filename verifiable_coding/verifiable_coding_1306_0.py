import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        count = [0] * 26
        for c in S:
            count[ord(c) - ord('A')] += 1
        
        # Check for "LTIME" and "EMITL"
        required = [0] * 26
        for c in "LTIME":
            required[ord(c) - ord('A')] += 1
        for c in "EMITL":
            required[ord(c) - ord('A')] += 1
        
        # Check if counts are sufficient
        possible = True
        for i in range(26):
            if count[i] < required[i]:
                possible = False
                break
        
        print("YES" if possible else "NO")

if __name__ == '__main__':
    solve()