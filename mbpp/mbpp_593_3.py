def check(candidate):
    assert candidate("216.08.094.196")==('216.8.94.196') 
    assert candidate("12.01.024")==('12.1.24') 
    assert candidate("216.08.094.0196")==('216.8.94.196') 


def remove_leading_zeros(ip_address):
    parts = ip_address.split('.')
    cleaned_parts = [str(int(part)) for part in parts]
    return '.'.join(cleaned_parts)

check(remove_leading_zeros)