import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for n in cases:
        # Bulbs that are ON at the end are those with perfect square numbers
        # Because they are toggled by factors, and only perfect squares have odd number of factors
        count = int(n**0.5)
        # Subtract the count of numbers divisible by 3
        # Numbers divisible by 3 and are perfect squares are those whose square is divisible by 3
        # So count of such numbers is floor(sqrt(n / 9))
        count -= int((n // 9)**0.5)
        print(count)

if __name__ == '__main__':
    solve()