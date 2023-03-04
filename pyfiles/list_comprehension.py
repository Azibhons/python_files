# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]
print(result)
# [0, 4, 16, 36, 64]
# Python list comprehension provide a concise way for creating lists. it consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: [EXPRESSION for ITEM in LIST <if CONDITIONAL>].
#The expression can be anything-any kind of object can go into a list.
#A list comprehension always returns a list.
