Feature: testing BDD

   Scenario: return Fizz if multiple of 3
      Given any integer number
      When the number is 3
      Then result should be Fizz

   Scenario: return Fizz if multiple of 5
      Given any integer number
      When the number is 5
      Then result should be Buzz

   Scenario: return FizzBuzz if multiple of 3 and 5
      Given any integer number
      When the number is 15
      Then result should be FizzBuzz

   Scenario: return number if not multiple of 3 and 5
      Given any integer number
      When the number is 1
      Then result should be 1
