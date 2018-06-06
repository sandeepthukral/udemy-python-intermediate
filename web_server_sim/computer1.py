import fake_database

CACHE = {}
last_file_resuts = []

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
  if len(last_file_resuts) == 5:
    last_file_resuts.pop(0)
  last_file_resuts.append((a,b,result))
  pass


def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    print(last_file_resuts)
    pass


def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    """
    key =(a, b)

    if key in CACHE:
      result = CACHE[key]
    else:
      result = fake_database.russian_peasant(a,b)
      updateLastMultiplied(a, b, result)
      CACHE[key] = result
    print result

    lastMultipliedHandler()
    pass
