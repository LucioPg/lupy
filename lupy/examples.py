"""Examples collection"""


try:
    from lupy.decorators import *
except ImportError:
    from decorators import *
try:
    from lupy.exceptions import *
except ImportError:
    from exceptions import *


@example_dec
def chained_comparison():
    """Example of Chained Comparison:
            '>>>b=6'
            '>>>print(4 < b < 7)'
            '>>> True'
            '>>>print(1 == b < 20)'
            '>>>False'
            """


@example_dec
def chained_funcs():
    """Chained function call:
        Calling different functions with same args based on condition
        def product(a, b):
            return a * b

        def add(a, b):
            return a + b

        b = True
        print((product if b else add)(5, 7))"""


@example_dec
class Employee:
    """
    example how to give a class object add capability

    a = Employee('Alice','EMP001',10000)
    b = Employee(Bob,EMP002,5000)
    if __name__ == '__main__':
        a = Employee('Alice','EMP001',10000)
        b = Employee('Bob','EMP002',10000)
        print(a + b)
    """
    def __init__(self, name, ID, salary):
        self.empName = name
        self.empID = ID
        self.empSalary = salary

    def __str__(self):
            return f'Employee({self.empName},{self.empID},{str(self.empSalary)})'

    def __repr__(self):
        return f'{self.empID} -- {self.empName}'

    def __add__(self, second_object):
        return self.empSalary + second_object.empSalary


@example_dec
def for_else_example():
    """For else example:

    else will be called if for loop does not reach the break statement

    a = [1,2,3,4,5]
    for el in a:
        if el == 0:
            break
    else:
        print('did not break out of the for loop')

    it can be used for limit the attempts to insert passwords"""


@example_dec
def merging_dicts_examples():
    """Merge dicts examples
    d1 = {'a': 1}
    d2 = {'b': 2}

    method 1:
    print({**d1, **d2})
    method 2:
    print(dict(d1.items() | d2.items()))
    method 3:
    d1.update(d2)
    print(d1)
    """


@example_dec
def swap_vals(a=5, b=10):
    """Swapping values:
        a, b = b, a
    return  a, b"""