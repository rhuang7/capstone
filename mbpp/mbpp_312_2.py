def check(candidate):
    assert candidate(5,12)==314.15926535897927
    assert candidate(10,15)==1570.7963267948965
    assert candidate(19,17)==6426.651371693521


def cone_volume(radius, height):
    import math
    return (1/3) * math.pi * radius ** 2 * height

check(cone_volume)