## string.maketrans(from, to)
##      Return a translation table suitable for passing to translate(),
##      that will map each character in from into the character at the
##      same position in to; from and to must have the same length.

## string.translate(s, table[, deletechars]) ***** Not In Python 3.x ******
##      Delete all characters from s that are in deletechars (if present),
##      and then translate the characters using table, which must be a
##      256-character string giving the translation for each character value,
##      indexed by its ordinal. If table is None, then only the character
##      deletion step is performed.


import string

table = string.maketrans('ABCDEF', '123456')
print 'BED FACED LOL'.translate(table)

enc_table = string.maketrans('ABCDEF', 'ZXTRSF')
dec_table = string.maketrans('ZXTRSF', 'ABCDEF')

enc = 'BED FACED'.translate(enc_table)
print enc

dec = enc.translate(dec_table)
print dec