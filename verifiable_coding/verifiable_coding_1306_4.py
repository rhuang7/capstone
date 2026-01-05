import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('A')] += 1
        
        # Check for "LTIME" and "EMITL"
        required = [ord('L') - ord('A'), ord('T') - ord('A'), ord('I') - ord('A'), ord('M') - ord('E') - ord('A'), ord('E') - ord('A')]
        # Check if we have enough characters for "LTIME" and "EMITL"
        for i in range(5):
            if count[required[i]] < 1:
                print("NO")
                break
        else:
            # Check if the remaining characters can be arranged
            # The total length of the string must be at least 10 (5 + 5)
            if len(s) < 10:
                print("NO")
            else:
                # Check if the remaining characters can be arranged in any way
                # We just need to ensure that the counts are sufficient for "LTIME" and "EMITL"
                # Since we have already checked that, and the total length is sufficient, it's possible
                print("YES")

if __name__ == '__main__':
    solve()