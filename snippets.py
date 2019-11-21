#1. Swap values between two variables
#In other languages, to swap values between two variables without using a third variable, we either have to use arithmetic 
# operators or bitwise XOR. In Python, it is much simpler, as shown below.
a = 5                               
b = 10
a, b = b, a
print(a) # 10                               
print(b) # 5


#2. Check if the given number is even
#The following function returns True if the given number is even, False otherwise.
def is_even(num):
  return num % 2 == 0
is_even(10) # True


#3. Split a multiline string into a list of lines
#The following function can be used for splitting a multiline string into a list of lines.
def split_lines(s):
  return s.split('\n')
split_lines('50\n python\n snippets') # ['50', ' python', ' snippets']


#4. Find memory used by an object
#The standard library’s sys module provides the getsizeof() function. That function accepts an object, 
# calls the object’s sizeof() method, and returns the result, so you can make your objects inspectable.
import sys
print(sys.getsizeof(5)) # 28
print(sys.getsizeof("Python")) # 55


#5. Reverse a string
#Python string library doesn’t support the built-in reverse() as done by other Python containers like list. 
# There are many approaches to reversing a string, of which the easiest way is making use of the slicing operator.
language = "python"                                
reversed_language = language[::-1] 
print(reversed_language) # nohtyp

#6. Print a string n times
#It is very easy to print a string n times without using loops, as shown below.
def repeat(string, n):
  return (string * n)
repeat('python', 3) # pythonpythonpython


#7. Check if a string is a palindrome
#The following function is used for checking if a string is a palindrome or not.
def palindrome(string):
    return string == string[::-1]
palindrome('python') # False


#8. Combine a list of strings into a single string
#The next snippet combines a list of strings into a single string.
strings = ['50', 'python', 'snippets']
print(','.join(strings)) # 50,python,snippets


#9. Find the first element of a list
#This function returns the first element of the passed list.
def head(list):
  return list[0]
print(head([1, 2, 3, 4, 5])) # 1


#10. Find elements that exist in either of the two lists
#This function returns every element that exists in either of the two lists.
def union(a,b):
  return list(set(a + b))
union([1, 2, 3, 4, 5], [6, 2, 8, 1, 4]) # [1,2,3,4,5,6,8]


#11. Find all the unique elements present in a given list
#This function returns the unique elements present in a given list.
def unique_elements(numbers):
  return list(set(numbers))
unique_elements([1, 2, 3, 2, 4]) # [1, 2, 3, 4]


#12. Find the average of a list of numbers
#This function returns the average of two or more numbers present in a list.
def average(*args):
  return sum(args, 0.0) / len(args)
average(5, 8, 2) # 5.0


#13. Check if a list contains all unique values
#This function checks if all the elements in a list are unique or not.
def unique(list):
    if len(list)==len(set(list)):
        print("All elements are unique")
    else:
        print("List has duplicates")
unique([1,2,3,4,5]) # All elements are unique


#14. Track frequency of elements in a list
#Python counter keeps track of the frequency of each element in the container. 
# Counter() returns a dictionary with elements as keys and frequency of its occurrence as its values.
from collections import Counter
list = [1, 2, 3, 2, 4, 3, 2, 3]
count = Counter(list)
print(count) # {2: 3, 3: 3, 1: 1, 4: 1}


#15. Find the most frequent element in a list
#This function returns the most frequent element that appears in a list.
def most_frequent(list):
    return max(set(list), key = list.count)
numbers = [1, 2, 3, 2, 4, 3, 1, 3]
most_frequent(numbers) # 3


#16. Convert an angle from degrees to radians
#The next function is used for converting an angle from degrees to radians.
import math
def degrees_to_radians(deg):
  return (deg * math.pi) / 180.0
degrees_to_radians(90) # 1.5707963267948966


#17. Calculate time taken to execute a piece of code
#The following snippet is used for calculating the time taken to execute a piece of code.
import time
start_time = time.time()
a,b = 5,10
c = a+b
end_time = time.time()
time_taken = (end_time- start_time)*(10**6)
print("Time taken in micro_seconds:", time_taken) # Time taken in micro_seconds: 39.577484130859375


#18. Find gcd of a list of numbers
#This function calculates the greatest common divisor of a list of numbers.
from functools import reduce
import math
def gcd(numbers):
  return reduce(math.gcd, numbers)
gcd([24,108,90]) # 6


#19. Find unique characters in a string
#This snippet can be used to find all the unique characters present in a string.
string = "abcbcabdb"   
unique = set(string)
new_string = ''.join(unique)
print(new_string) # abcd


#20. Use lambda functions
#Lambda is an anonymous function with the capability of holding a single expression only.
x = lambda a, b, c : a + b + c
print(x(5, 10, 20)) # 35


#21. Use map functions
#This function returns a list of the results after applying the given function to each item of a given iterable(list, tuple, etc.)
def multiply(n): 
    return n * n 
  
list = [1, 2, 3]
result = map(multiply, list)
print(result)
#print(list(result)) # {1, 4, 9}


#22. Use filter functions
#This function filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
arr = [1, 2, 3, 4, 5]
#arr = list(filter(lambda x : x%2 == 0, arr))
arr = (filter(lambda x : x%2 == 0, arr))
print (arr) # [2, 4]


#23. Use list comprehensions
#List comprehensions provide us with a simple way to create a list based on some iterable. 
# During the creation, elements from the iterable can be conditionally included in the new list and transformed as needed.
numbers = [1, 2, 3]
squares = [number**2 for number in numbers]
print(squares) # [1, 4, 9]


#24. Use slicing operator
#Slicing is used to extract a continuous sequence or subsequence of elements from a given sequence. 
# The following function is used for concatenating the results of two slicing operations. 
# First, we are slicing the list from index d to end, then from start to index d.
def rotate(arr, d):
  return arr[d:] + arr[:d]
  
if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  arr = rotate(arr, 2)
  print (arr) # [3, 4, 5, 1, 2]


#25. Use chained function call
#The final snippet is used to call multiple functions from a single line and evaluate the result.
def add(a, b):
    return a + b
def subtract(a, b):   
    return a - b
a, b = 5, 10
print((subtract if a > b else add)(a, b)) # 15