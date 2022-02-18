import pytest

pytest.main([__file__, '-v', '-p', 'no:warnings'])

# Write your code and tests below

def fizzbuzz(n):
  result = ""

  if n % 3 == 0 and n % 5 == 0:
    result = "FizzBuzz"
  elif n % 3 == 0:
    result = "Fizz"
  elif n % 5 == 0:
    result = "Buzz"
  else:
    result = str(n)

  return result


def test_number_divisible_by_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"


def test_number_divisible_by_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"


def test_number_divisible_by_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


def test_simple_numbers():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"

