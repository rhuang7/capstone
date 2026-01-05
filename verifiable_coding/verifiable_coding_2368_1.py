import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find the minimum possible a_i and b_i for each gift
        # The final a_i and b_i must be such that all a_i are equal and all b_i are equal
        # So we need to find the minimum a_i and b_i that can be achieved by eating from the gifts
        
        # For each gift, the minimum possible a_i is the minimum of a_i and b_i
        # Because we can eat either candy or orange or both to reduce the values
        # So the minimum a_i for all gifts is the minimum of the minimum of a_i and b_i for each gift
        
        min_a = min(min(a[i], b[i]) for i in range(n))
        min_b = min(min(a[i], b[i]) for i in range(n))
        
        # Calculate the total moves needed
        total_moves = 0
        for i in range(n):
            # For a_i: we can eat (a[i] - min_a) candies or (a[i] - min_a) oranges or a combination
            # But since we can eat both, the minimum moves is (a[i] - min_a) + (b[i] - min_b)
            # Because we can eat one candy and one orange per move to reduce both
            # So the total moves for this gift is (a[i] - min_a) + (b[i] - min_b)
            total_moves += (a[i] - min_a) + (b[i] - min_b)
        
        results.append(total_moves)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()