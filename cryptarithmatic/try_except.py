

userDefined = '23'

try:
  a = int(userDefined)
except ValueError:
  a = int(0)
except:
  print 'something went wrong'
finally:
  print "a = {}".format(a)