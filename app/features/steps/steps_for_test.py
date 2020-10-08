from behave import given, when, then
from src.main import fizzbuzz


@given('any integer number')
def step_impl_given(context):
    pass


@when('the number is {number}')
def step_impl_when(context, number):
    context.number = int(number)


@then('result should be {result}')
def step_impl_then(context, result):
    assert fizzbuzz(context.number) == result
