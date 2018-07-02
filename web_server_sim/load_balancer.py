### SERVER NAMES
SERVERS = ['APP1', 'APP2', 'APP3']
count = -1

def get_server():
  global count
  count = count + 1
  return SERVERS[count % len(SERVERS)]

### testing the function
if __name__ == '__main__':
  for i in range(9):
    print get_server()