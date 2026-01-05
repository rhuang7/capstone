import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        snake_count = s.count('s')
        mongoose_count = s.count('m')
        
        # Maximum number of snakes that can be eaten is the number of consecutive 'm's
        # But since each 'm' can eat at most one neighbor 's', the maximum snakes eaten is the number of 'm's
        # However, if there are more 'm's than 's's, the maximum snakes eaten is 's' count
        # So the maximum snakes eaten is min(mongoose_count, snake_count)
        max_snakes_eaten = min(mongoose_count, snake_count)
        
        remaining_snakes = snake_count - max_snakes_eaten
        remaining_mongostes = mongoose_count
        
        if remaining_snakes > remaining_mongostes:
            print("snakes")
        elif remaining_snakes < remaining_mongostes:
            print("mongooses")
        else:
            print("tie")

if __name__ == '__main__':
    solve()