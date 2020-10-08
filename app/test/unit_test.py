from src.main import fizzbuzz


def test_returnnumberifnotmultipleofthreeorfive():
    assert fizzbuzz(1) == '1'


def test_returnfizzifmultipleofthree():
    assert fizzbuzz(3) == 'Fizz'


def test_returnfizzifmultipleoffive():
    assert fizzbuzz(5) == 'Buzz'


def test_returnfizzifmultipleofthreeandfive():
    assert fizzbuzz(15) == 'FizzBuzz'
