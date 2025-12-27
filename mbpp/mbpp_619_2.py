def check(candidate):
    assert candidate('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert candidate('Avengers124Assemble') == 'AvengersAssemble124'
    assert candidate('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'


def move_numbers_to_string(input_string):
    return ''.join(char for char in input_string if char.isdigit())

check(move_numbers_to_string)