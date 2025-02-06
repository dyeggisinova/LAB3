"""
def reverse_words():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    reversed_sentence = " ".join(words[::-1])

    return reversed_sentence
result = reverse_words()
print("Reversed sentence: ",result)
"""
"""
def has_33(nums):

    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3: 
            return True
    return False 

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
"""
"""
def spy_game(nums):
   
    sequence = [0, 0, 7]
    for num in nums:
       
        if num == sequence[0]:
           
            sequence.pop(0)
       
        if not sequence:
            return True
    
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7])) 
"""
"""
import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = 5
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")
"""
"""
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print(result)
"""