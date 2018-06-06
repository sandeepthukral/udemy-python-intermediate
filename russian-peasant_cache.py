import time

CACHE = {}

def russian_peasant(a, b):

  key = (a,b)

  z = 0

  if key in CACHE:
    z = CACHE[key]
  else :
    x = a; y = b
    while x > 0:
      if x % 2 == 1: z = z + y
      y = y << 1
      x = x >> 1
    CACHE[key] = z

  return z

assert russian_peasant(238, 13) == 3094

start_time = time.time()
print russian_peasant(238, 13)
print "Russian peasant ran in %f seconds" % (time.time() - start_time)

start_time = time.time()
print russian_peasant(238, 13)
print "Russian peasant ran in %f seconds" % (time.time() - start_time)

start_time = time.time()
print russian_peasant(238, 13)
print "Russian peasant ran in %f seconds" % (time.time() - start_time)