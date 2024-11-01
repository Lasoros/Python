from timeit import timeit #allows calcualtion of execution time of python code

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less. . .")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))