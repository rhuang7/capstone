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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = data[idx]
        idx += 1
        
        max_pizza_time = 0
        current_streak = 0
        zero_positions = []
        
        for i in range(N):
            if A[i] == '0':
                zero_positions.append(i)
        
        for i in range(len(zero_positions)):
            zero_idx = zero_positions[i]
            if i + 1 < len(zero_positions):
                next_zero_idx = zero_positions[i + 1]
                if next_zero_idx - zero_idx - 1 >= K:
                    # Can cover the gap between two zeros with K length
                    # The pizza time would be (next_zero_idx - zero_idx - 1) + 1
                    pizza_time = (next_zero_idx - zero_idx - 1) + 1
                    max_pizza_time = max(max_pizza_time, pizza_time)
            else:
                # Check if the last zero can be covered
                if zero_idx + K <= N:
                    pizza_time = K
                    max_pizza_time = max(max_pizza_time, pizza_time)
        
        # Check for sequences of 1s
        current_streak = 0
        for c in A:
            if c == '1':
                current_streak += 1
                max_pizza_time = max(max_pizza_time, current_streak)
            else:
                current_streak = 0
        
        results.append(str(max_pizza_time))
    
    print('\n'.join(results)) 

if __name__ == '__main__':
    solve()