"""
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_input = input("Enter the gram: ")
grams = float(grams_input)
ounces = grams_to_ounces(grams)
print(f"{grams} is equal to {ounces} ounces.")
"""
"""
def to_centigrade(farenheit):
    centigrade = (5/9)*(farenheit - 32)
    return centigrade

faren_input = input("Enter the value of farenheit: ")
farenheit = float(faren_input)
C = to_centigrade(farenheit)
print(f"{farenheit} is equal to {C} in centigrade")

"""

"""
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    
    return x, y

numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)

print(f"There are {chickens} chickens and {rabbits} rabbits.")
"""
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [10, 15, 23, 37, 40, 41, 50, 60, 2, 3]
primes = filter_prime(numbers)
print(primes)
"""

import itertools
def print_permutations():
    user_input = input("Enter a string: ")
    
   
    permutations = itertools.permutations(user_input)
    
    
    for perm in permutations:
        print("".join(perm))
print_permutations()