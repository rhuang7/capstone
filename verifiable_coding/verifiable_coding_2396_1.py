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
            half = len(s) // 2
            first = s[:half]
            second = s[half:]
            if first.count(c) == half:
                return is_good(second, chr(ord(c) + 1))
            if second.count(c) == half:
                return is_good(first, chr(ord(c) + 1))
            return False
        
        def min_moves(s, c):
            if len(s) == 1:
                return 0 if s[0] == c else 1
            half = len(s) // 2
            first = s[:half]
            second = s[half:]
            if first.count(c) == half:
                return min_moves(second, chr(ord(c) + 1))
            if second.count(c) == half:
                return min_moves(first, chr(ord(c) + 1))
            return min(min_moves(first, chr(ord(c) + 1)) + half - first.count(c), min_moves(second, chr(ord(c) + 1)) + half - second.count(c))
        
        print(min_moves(s, 'a'))

if __name__ == '__main__':
    solve()