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
        
        # Function to check if a substring is c-good
        def is_c_good(s, c, start, end):
            if start == end:
                return s[start] == c
            mid = (start + end) // 2
            # Check condition 1: first half is c and second half is (c+1)-good
            if all(s[i] == c for i in range(start, mid + 1)) and is_c_good(s, chr(ord(c) + 1), mid + 1, end):
                return True
            # Check condition 2: second half is c and first half is (c+1)-good
            if all(s[i] == c for i in range(mid + 1, end + 1)) and is_c_good(s, chr(ord(c) + 1), start, mid):
                return True
            return False
        
        # Function to calculate minimum changes to make a substring c-good
        def min_changes(s, c, start, end):
            if start == end:
                return 0 if s[start] == c else 1
            mid = (start + end) // 2
            # Check condition 1: first half is c and second half is (c+1)-good
            if all(s[i] == c for i in range(start, mid + 1)):
                changes = 0
                for i in range(mid + 1, end + 1):
                    if s[i] != chr(ord(c) + 1):
                        changes += 1
                changes += min_changes(s, chr(ord(c) + 1), mid + 1, end)
                return changes
            # Check condition 2: second half is c and first half is (c+1)-good
            if all(s[i] == c for i in range(mid + 1, end + 1)):
                changes = 0
                for i in range(start, mid + 1):
                    if s[i] != chr(ord(c) + 1):
                        changes += 1
                changes += min_changes(s, chr(ord(c) + 1), start, mid)
                return changes
            # If neither condition is satisfied, try both and return minimum
            changes1 = 0
            for i in range(start, mid + 1):
                if s[i] != chr(ord(c) + 1):
                    changes1 += 1
            changes1 += min_changes(s, chr(ord(c) + 1), start, mid)
            
            changes2 = 0
            for i in range(mid + 1, end + 1):
                if s[i] != chr(ord(c) + 1):
                    changes2 += 1
            changes2 += min_changes(s, chr(ord(c) + 1), mid + 1, end)
            
            return min(changes1, changes2)
        
        result = min_changes(s, 'a', 0, n - 1)
        print(result)