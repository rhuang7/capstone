import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    n1 = int(data[idx])
    idx += 1
    n2 = int(data[idx])
    idx += 1
    n3 = int(data[idx])
    idx += 1
    
    list1 = set()
    for _ in range(n1):
        list1.add(int(data[idx]))
        idx += 1
    
    list2 = set()
    for _ in range(n2):
        list2.add(int(data[idx]))
        idx += 1
    
    list3 = set()
    for _ in range(n3):
        list3.add(int(data[idx]))
        idx += 1
    
    common = list1 & list2 & list3
    common = sorted(common)
    
    print(len(common))
    for num in common:
        print(num)
        
if __name__ == '__main__':
    solve()