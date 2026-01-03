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
        count1 = 0
        count2 = 0
        for i in range(n):
            if s[i] != target1[i]:
                count1 += 1
            if s[i] != target2[i]:
                count2 += 1
        
        # The minimum number of operations is the minimum of the two counts divided by 2
        # Because each operation can fix two mismatches
        print(min(count1, count2) // 2)

if __name__ == '__main__':
    solve()