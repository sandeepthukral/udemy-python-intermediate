# -*- coding: utf-8 -*-

##  eval(expression[, globals[, locals]])
##      The arguments are a string and optional globals and locals.
##      If provided, globals must be a dictionary. If provided, locals can be
##      any mapping object.

##      Changed in version 2.4: formerly locals was required to be a dictionary.

##      The expression argument is parsed and evaluated as a Python expression
##      (technically speaking, a condition list) using the globals and locals
##      dictionaries as global and local namespace. If the globals dictionary
##      is present and lacks ‘__builtins__’, the current globals are copied into
##      globals before expression is parsed. This means that expression normally
##      has full access to the standard __builtin__ module and restricted
##      environments are propagated. If the locals dictionary is omitted it
##      defaults to the globals dictionary. If both dictionaries are omitted,
##      the expression is executed in the environment where eval() is called.
##      The return value is the result of the evaluated expression. Syntax
##      errors are reported as exceptions. Example:

x = 3
print eval('x*3')
