from typing import List


class Multiple:
    def __init__(self, number: int):
        self.number = number

    def ismultipleofallnumbersinlist(self, listofmultiple: List[int]):
        return not(False in [self.number % n == 0 for n in listofmultiple])


def fizzbuzz(number: int) -> str:
    """Returns
    - Fizz if number is a multiple of 3,
    - Buzz if multiple of 5,
    - FizzBuzz if multile of 3 and 5,
    - the number itself in all other cases

    Args:
        number (int): number to be checked
    """

    multiple = Multiple(number)
    if multiple.ismultipleofallnumbersinlist([3, 5]):
        result = 'FizzBuzz'
    elif multiple.ismultipleofallnumbersinlist([3]):
        result = 'Fizz'
    elif multiple.ismultipleofallnumbersinlist([5]):
        result = 'Buzz'
    else:
        result = str(number)

    return result
