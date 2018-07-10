import fake_database
from memcache_homework import Memcache

cache = Memcache()
last_five_calculations = []
KEY_LAST_FIVE = 'lastFive'

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):

  lastFiveList = cache.get(KEY_LAST_FIVE)
  if lastFiveList:
    if len(lastFiveList) >= 5:
      lastFiveList = lastFiveList[1:]
    lastFiveList.append('{}x{}={}'.format(a,b,result))
  else:
    # There is no cache so set one
    cache.set(KEY_LAST_FIVE,['{}x{}={}'.format(a,b,result)])

def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    lastFive = cache.get(KEY_LAST_FIVE)
    if lastFive:
      print 'Last five results : {}'.format(lastFive)
    else:
      print 'Russian not used before'
    pass


def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    """
    key = (a,b)
    cachedAnswer = cache.get(key)

    if not cachedAnswer:
      result = fake_database.russian_peasant(a,b)
      updateLastMultiplied(a, b, result)
      cache.set(key, result)
      cachedAnswer = cache.get(key)

    print 'Last result : {}'.format(cachedAnswer)

if __name__ == '__main__':
    multiplyHandler(2,6)
    multiplyHandler(5,6)
    multiplyHandler(10,6)
    multiplyHandler(23,6)
    multiplyHandler(4,6)
    multiplyHandler(11,6)
    multiplyHandler(23,6)
    multiplyHandler(200,6)