def check(candidate):
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]


def find_expensive_items(data, n):
    import heapq
    
    # Use a max-heap to find the n most expensive items
    # Convert the data into a list of tuples (price, item)
    # Since Python's heapq module implements a min-heap, we store negative prices
    heap = [(-price, item) for price, item in data]
    
    # Heapify the list
    heapq.heapify(heap)
    
    # Extract the n most expensive items
    expensive_items = []
    for _ in range(n):
        if not heap:
            break
        price, item = heapq.heappop(heap)
        expensive_items.append((abs(price), item))
    
    return expensive_items

check(find_expensive_items)