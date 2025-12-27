def check(candidate):
    assert candidate([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
    assert candidate([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  
    assert candidate([(), (), ('',), ("java")])==[('',),("java") ]  


def remove_empty_tuples(tuples_list):
    return [t for t in tuples_list if t != ()]

check(remove_empty_tuples)