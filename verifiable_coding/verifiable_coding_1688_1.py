import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        lis = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Construct the number
        num = []
        prev = 0
        for i in range(n):
            if i == 0:
                # First digit can be anything, but we'll choose 1 to avoid leading zero
                num.append('1')
                prev = 1
            else:
                # The current LIS value must be greater than the previous LIS value or equal
                # We want to choose a digit that is larger than the previous digit if possible
                # to ensure the LIS is correct
                if lis[i] > lis[i - 1]:
                    # Choose a digit larger than the previous digit
                    num.append(str(prev + 1))
                    prev = prev + 1
                else:
                    # Choose a digit smaller than or equal to the previous digit
                    num.append(str(prev - 1))
                    prev = prev - 1
        
        results.append(''.join(num))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()