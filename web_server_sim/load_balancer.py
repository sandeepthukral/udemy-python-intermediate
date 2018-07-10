### SERVER NAMES
#SERVERS = ['APP1', 'APP2', 'APP3']
# count = -1

# def get_server():
#   global count
#   count = count + 1
#   return SERVERS[count % len(SERVERS)]

# import itertools
# cycle = itertools.cycle(SERVERS)

# def get_server():
#   global cycle
#   return cycle.next()

# def get_server():
#   try:
#     return next(get_server.s)
#   except StopIteration:
#     get_server.s = iter(SERVERS)
#     return next(get_server.s)
# setattr(get_server, 's', iter(SERVERS))

import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]
count = -1

def get_server():
  global count
  count = count + 1
  return SERVERS[count % len(SERVERS)]

### testing the function
if __name__ == '__main__':
  from random import randint

  for i in range(15):
    z = randint(1,3)
    a = [44, 85, 123][z%3]
    b = [54,15,32][z%3]
    # a = randint(5,99)
    # b = randint(5,99)


    server = get_server()

    print server.printName()
    server.multiplyHandler(a,b)
    server.lastMultipliedHandler()
    print " "