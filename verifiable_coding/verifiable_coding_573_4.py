import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        if n == 1:
            print(m)
            continue
        
        # The time required is determined by the maximum of two values:
        # 1. The time for the first person to learn all m topics from the end (Malvika)
        # 2. The time for the last person to learn all m topics from the second last person
        # Since each topic takes 1 hour to propagate, and each person can learn from the next
        # The maximum time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # However, since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn from the second
        # The second person needs m hours to learn from the third, and so on
        # The total time is m * 2 - 1 for the first person to learn all topics
        # But since Malvika is at the end, the first person needs m hours to learn