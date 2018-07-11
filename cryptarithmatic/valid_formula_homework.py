
# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string

import re

def noFirstZero(formula):
    ##: formula is a string
    return not re.search(r'\b0[0-9]', formula)

def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    """
    try:
        ## your code here
        if re.search(r'\b0[0-9]', formula):
          return False
        return eval(formula)
    except ArithmeticError:
        ## your code here
        return False
    except:
        ## your code here
        return False

assert valid('123+123==246') is True
assert valid('123+123==426') is False
assert valid('012+123==456') is False