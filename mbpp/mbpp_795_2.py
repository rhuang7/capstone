def check(candidate):
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-1', 'price': 101.1}]
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],2)==[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]
    assert candidate([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]


def find_cheapest_items(dataset, n):
    import heapq
    
    # Use a heap to find the n cheapest items
    # Convert the dataset into a list of tuples (price, item)
    # Then heapify the list to get the smallest prices
    heap = [(price, item) for item, price in dataset]
    heapq.heapify(heap)
    
    # Extract the n cheapest items
    cheapest_items = []
    for _ in range(n):
        if heap:
            cheapest_items.append(heapq.heappop(heap))
    
    return cheapest_items

check(find_cheapest_items)