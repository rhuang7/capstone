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
        is_alt_01 = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                is_alt_01 = False
                break
        if is_alt_01:
            print(0)
            continue
        
        # Check if the string is already alternating starting with 1
        is_alt_10 = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                is_alt_10 = False
                break
        if is_alt_10:
            print(0)
            continue
        
        # Count the number of mismatches for both patterns
        count_01 = 0
        count_10 = 0
        for i in range(n):
            if i % 2 == 0:
                expected = '0'
            else:
                expected = '1'
            if s[i] != expected:
                count_01 += 1
        
        for i in range(n):
            if i % 2 == 0:
                expected = '1'
            else:
                expected = '0'
            if s[i] != expected:
                count_10 += 1
        
        # The minimum number of operations is the minimum of the two counts
        # Because each mismatch can be fixed with one operation
        print(min(count_01, count_10))
        
if __name__ == '__main__':
    solve()