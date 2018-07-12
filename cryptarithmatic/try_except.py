
userDefined = 'b'

try:
  a = int(userDefined)
except ValueError:
  print 'Error 1'
except Exception:
  print 'Error 0'
except:
  print 'Error -1'
else:
  print "a = {}".format(a)