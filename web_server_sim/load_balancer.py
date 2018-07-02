### SERVER NAMES
SERVERS = ['APP1', 'APP2', 'APP3']
# count = -1

# def get_server():
#   global count
#   count = count + 1
#   return SERVERS[count % len(SERVERS)]

import itertools
cycle = itertools.cycle(SERVERS)

def get_server():
  global cycle
  return cycle.next()

### testing the function
if __name__ == '__main__':
  for i in range(9):
    print get_server()