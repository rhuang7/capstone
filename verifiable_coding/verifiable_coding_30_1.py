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
        correct1 = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                correct1 = False
                break
        if correct1:
            print(0)
            continue
        
        # Check if the string is already alternating starting with 1
        correct2 = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                correct2 = False
                break
        if correct2:
            print(0)
            continue
        
        # Count the number of mismatches for both patterns
        count1 = 0
        count2 = 0
        for i in range(n):
            if i % 2 == 0:
                expected = '0'
            else:
                expected = '1'
            if s[i] != expected:
                count1 += 1
        
        for i in range(n):
            if i % 2 == 0:
                expected = '1'
            else:
                expected = '0'
            if s[i] != expected:
                count2 += 1
        
        # The minimum number of operations is the minimum of the two counts divided by 2
        # Because each operation can fix two mismatches
        print(min(count1, count2) // 2)

if __name__ == '__main__':
    solve()