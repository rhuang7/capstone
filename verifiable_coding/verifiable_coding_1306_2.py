import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    required = "LTIMEEMITL"
    for s in cases:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('A')] += 1
        required_count = [0] * 26
        for c in required:
            required_count[ord(c) - ord('A')] += 1
        valid = True
        for i in range(26):
            if count[i] < required_count[i]:
                valid = False
                break
        print("YES" if valid else "NO")

if __name__ == '__main__':
    solve()