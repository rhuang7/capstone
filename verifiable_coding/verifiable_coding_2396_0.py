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
        def is_c_good(sub, c):
            if len(sub) == 1:
                return sub == c
            mid = len(sub) // 2
            first_half = sub[:mid]
            second_half = sub[mid:]
            # Check condition 2: first half is c and second is (c+1)-good
            if first_half == c * mid and is_c_good(second_half, chr(ord(c) + 1)):
                return True
            # Check condition 3: second half is c and first is (c+1)-good
            if second_half == c * mid and is_c_good(first_half, chr(ord(c) + 1)):
                return True
            return False
        
        # Function to compute minimum changes to make a substring c-good
        def min_changes(sub, c):
            if len(sub) == 1:
                return 0 if sub == c else 1
            mid = len(sub) // 2
            first_half = sub[:mid]
            second_half = sub[mid:]
            # Check condition 2: first half is c and second is (c+1)-good
            if first_half == c * mid:
                changes = min_changes(second_half, chr(ord(c) + 1))
                return changes
            # Check condition 3: second half is c and first is (c+1)-good
            if second_half == c * mid:
                changes = min_changes(first_half, chr(ord(c) + 1))
                return changes
            # Otherwise, try to make first half c and second (c+1)-good
            changes_first = 0
            for ch in first_half:
                if ch != c:
                    changes_first += 1
            changes_second = min_changes(second_half, chr(ord(c) + 1))
            total = changes_first + changes_second
            # Try to make second half c and first (c+1)-good
            changes_second2 = 0
            for ch in second_half:
                if ch != c:
                    changes_second2 += 1
            changes_first2 = min_changes(first_half, chr(ord(c) + 1))
            total2 = changes_second2 + changes_first2
            return min(total, total2)
        
        # Compute the minimum changes for the entire string to be 'a'-good
        result = min_changes(s, 'a')
        print(result)

if __name__ == '__main__':
    solve()