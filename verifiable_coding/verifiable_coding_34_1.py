import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    seg = [6, 2, 5, 5, 4, 5, 3, 7, 6, 6]  # segments for digits 0-9
    
    for n in cases:
        # Maximize the number of digits by using the digit with the least segments
        # The digit with the least segments is 1 (2 segments)
        # So the maximum number of digits is n // 2
        max_digits = n // 2
        # The best digit to use is 1 (as it uses 2 segments and is the smallest possible)
        # But if n is odd, we can use one more 1 (using 2 segments) and then use the remaining segments for another digit
        # However, since we want the largest possible number, we should use as many 1s as possible
        # But if n is odd, we can use one more 1 and then use the remaining segments for a 7 (which uses 3 segments)
        # So the maximum number is '1' * (max_digits) if n is even, else '1' * (max_digits) + '7'
        if n % 2 == 0:
            print('1' * (n // 2))
        else:
            print('1' * (n // 2) + '7')

if __name__ == '__main__':
    solve()