def add_num(a,b):
  return a + b

def test_add_num():
  assert add_num(34, 67) == 101
  assert add_num(34, 67) == 100
  return "All tests are OK"

print test_add_num()