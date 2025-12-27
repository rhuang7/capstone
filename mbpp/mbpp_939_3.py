def check(candidate):
    assert candidate([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}])==[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
    assert candidate([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])==([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])
    assert candidate([{'make':'micromax','model':40,'color':'grey'},{'make':'poco','model':60,'color':'blue'}])==([{'make':'poco','model':60,'color':'blue'},{'make':'micromax','model':40,'color':'grey'}])


def sort_dict_list(list_of_dicts, key_func):
    return sorted(list_of_dicts, key=key_func)

check(sort_dict_list)