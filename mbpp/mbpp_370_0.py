def check(candidate):
    assert candidate([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])==[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
    assert candidate([('item1', '15'), ('item2', '10'), ('item3', '20')])==[('item3', '20'), ('item1', '15'), ('item2', '10')] 
    assert candidate([('item1', '5'), ('item2', '10'), ('item3', '14')])==[('item3', '14'), ('item2', '10'), ('item1', '5')] 


def sort_tuple_by_float(tup):
    return sorted(tup, key=lambda x: x[1])

check(sort_tuple_by_float)