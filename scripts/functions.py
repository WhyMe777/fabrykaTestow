######################################################################
# przykład 2
######################################################################

def divide(divident, divisor):
    if(divisor == 0):
        return False
    else:
        return divident / divisor

print(divide(5,0))
print(divide(10,2))


######################################################################
# przykład 3
######################################################################

def my_function(arg1 , arg2 = "Opel"):
    return f'{arg1} {arg2}'

print(my_function(arg1='samochód ', arg2= "Skoda"))


######################################################################
# przykład 4
######################################################################

from functools import partial

def division(x,y):
    return x/y

divide_by_two = partial(division,2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))
