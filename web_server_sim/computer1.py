import fake_database

CACHE = {}
last_five_calculations = []

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
  if len(last_five_calculations) == 5:
    last_five_calculations.pop(0)
  last_five_calculations.append((a,b,result))
  pass


def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    list_last_results = [x[2] for x in last_five_calculations]
    print 'Last five results : {}'.format(list_last_results)
    print "--"*13
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
    print 'Last result : {}'.format(result)

    lastMultipliedHandler()
    pass
