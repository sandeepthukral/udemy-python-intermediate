import copy
import time

def russian_peasant(a, b):

  num1 = copy.copy(a)
  num2 = copy.copy(b)

  numbers_to_sum = []

  # do till num1 is greater than or equal to 1
  while num1 >= 1:
    # If num1 is odd, add num2 to the list of numbers to sum
    if (num1 % 2 != 0):
      numbers_to_sum.append(num2)

    # multiply num2 by 2 and divide num1 by 2, keeing only the integral value
    num1 = num1 // 2
    num2 = num2 * 2

  print 'Hit DB!'
  return sum(numbers_to_sum)

def test_russian():
  print russian_peasant(283,13)
  assert russian_peasant(238, 13) == 3094

if __name__ == "__main__":
  test_russian()