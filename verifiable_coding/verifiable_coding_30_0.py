import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # Check if the string is already alternating
        target1 = '01' * (n // 2)
        target2 = '10' * (n // 2)
        
        if s == target1 or s == target2:
            print(0)
            continue
        
        # Count the number of mismatches for both targets
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if s[i] != target1[i]:
                cnt1 += 1
            if s[i] != target2[i]:
                cnt2 += 1
        
        # The minimum number of operations is the minimum of the two counts
        print(min(cnt1, cnt2) // 2)

if __name__ == '__main__':
    solve()