import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        snake_count = s.count('s')
        mongoose_count = s.count('m')
        
        # Maximum number of snakes that can be eaten is the number of consecutive 'm's
        # But since each 'm' can eat at most one neighbor, it's the number of 'm's
        # But we can only eat one snake per mongoose, so the maximum number of snakes that can be eaten is the number of 'm's
        # However, if there are more 'm's than 's's, then all 's's can be eaten
        # So the final count is:
        final_snakes = snake_count - min(mongoose_count, snake_count)
        final_mongoose = mongoose_count
        
        if final_snakes > final_mongoose:
            print("snakes")
        elif final_snakes < final_mongoose:
            print("mongooses")
        else:
            print("tie")

if __name__ == '__main__':
    solve()