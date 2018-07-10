

"TWO + TWO == FOUR"
"123 + 123 == 4567"

import re

def noFirstZero(formula):
    ##: formula is a string
    return not re.search(r'\b0[0-9]', formula)

def test_noFirstZero(formulae, results):
    for formula, result in zip(formulae, results):
        assert noFirstZero(formula) == result

L = ['123','406','023', '543 0453', '087 65', '00', '432 123']
R = [True, True, False, False, False, False, True]
test_noFirstZero(L, R)



