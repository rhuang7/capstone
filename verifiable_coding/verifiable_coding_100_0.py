import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        r = int(data[index])
        g = int(data[index+1])
        b = int(data[index+2])
        index += 3
        
        # The maximum number of days is determined by the sum of the two smaller piles
        # because Tanya can eat one candy from each of two piles each day.
        # The maximum possible is (sum of two smaller piles) // 2
        # But if the sum of all three is odd, the maximum is (sum of all three - 1) // 2
        # However, the correct formula is min((r + g + b) // 2, (sum of two smaller piles))
        # So we sort the numbers and compute accordingly
        a, b, c = sorted([r, g, b])
        total = a + b + c
        if total % 2 == 1:
            total -= 1
        result = total // 2
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()