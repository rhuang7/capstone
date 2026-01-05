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
        # But each 'm' can eat at most one neighbor 's'
        # So the maximum number of snakes that can be eaten is the number of 'm's
        # But we can't eat more than the number of snakes
        max_eaten = min(mongoose_count, snake_count)
        
        # After eating, the remaining snakes and mongooses
        remaining_snakes = snake_count - max_eaten
        remaining_mongostes = mongoose_count
        
        if remaining_snakes > remaining_mongostes:
            print("snakes")
        elif remaining_snakes < remaining_mongostes:
            print("mongooses")
        else:
            print("tie")

if __name__ == '__main__':
    solve()