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
        
        def is_good(s, c):
            if len(s) == 1:
                return s[0] == c
            mid = len(s) // 2
            first = s[:mid]
            second = s[mid:]
            if first == c * mid:
                return is_good(second, chr(ord(c) + 1))
            if second == c * mid:
                return is_good(first, chr(ord(c) + 1))
            return False
        
        def min_changes(s, c):
            if len(s) == 1:
                return 0 if s[0] == c else 1
            mid = len(s) // 2
            first = s[:mid]
            second = s[mid:]
            if first == c * mid:
                return min_changes(second, chr(ord(c) + 1))
            if second == c * mid:
                return min_changes(first, chr(ord(c) + 1))
            return min(
                min_changes(first, chr(ord(c) + 1)) + mid - sum(1 for ch in second if ch == c),
                min_changes(second, chr(ord(c) + 1)) + mid - sum(1 for ch in first if ch == c)
            )
        
        print(min_changes(s, 'a'))

if __name__ == '__main__':
    solve()