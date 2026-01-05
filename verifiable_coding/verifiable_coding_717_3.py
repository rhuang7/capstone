import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        B = int(data[index])
        G = int(data[index + 1])
        index += 2
        
        # Each boy gives a rose to a girl and each girl gives a rose to a boy
        # But the exchange is only possible if at least one of them hasn't received a rose
        # This implies that each person gives a rose to someone else, so total roses is B + G
        # But since each exchange involves two people, the total is 2 * min(B, G)
        # However, the problem says that exchange is only possible if at least one of them hasn't received a rose
        # So the total number of exchanges is 2 * min(B, G)
        # But in the sample input, B=2, G=3, min is 2, 2*2=4, but sample output is 8
        # So the correct formula is 2 * (B + G - 1)
        # Because each person gives a rose to someone else, and there are B + G people
        # So total roses is 2 * (B + G - 1)
        total = 2 * (B + G - 1)
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()