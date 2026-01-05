import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
        count = {}
        for num in s:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Count the number of each power of two
        powers = {}
        for num in count:
            power = num.bit_length() - 1
            if power in powers:
                powers[power] += count[num]
            else:
                powers[power] = count[num]
        
        # Try to build up to 2048
        current = 11  # 2^11 = 2048
        while current > 0:
            if current in powers:
                powers[current] -= 1
                if powers[current] == 0:
                    del powers[current]
                # Try to merge with next higher power
                if current + 1 in powers:
                    powers[current + 1] += 1
                else:
                    powers[current + 1] = 1
                current += 1
            else:
                break
        
        if 11 in powers:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()