def reverse_string():
    print("Program: Reverse a String")
    print("""
def reverse_string(s):
    return s[::-1]""")
    print("Test Case 1: reverse_string('hello') -> 'olleh'")
    print("Test Case 2: reverse_string('Python') -> 'nohtyP'")
    print("Explanation: Uses Python slicing to reverse the string.")

def check_even_odd():
    print("Program: Check Even or Odd")
    print("""
def is_even(n):
    return n % 2 == 0""")
    print("Test Case 1: is_even(5) -> False (Odd)")
    print("Test Case 2: is_even(8) -> True (Even)")
    print("Explanation: A number is even if divisible by 2.")

def factorial_recursion():
    print("Program: Factorial using Recursion")
    print("""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)""")
    print("Test Case 1: factorial(4) -> 24")
    print("Test Case 2: factorial(5) -> 120")
    print("Explanation: Uses recursion to multiply each number down to 1.")

def is_palindrome():
    print("Program: Check Palindrome")
    print("""
def is_palindrome(s):
    return s == s[::-1]""")
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Compares string to its reverse.")

def fibonacci_series():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b""")
    print("Test Case 1: fibonacci(6) -> 0 1 1 2 3 5")
    print("Test Case 2: fibonacci(4) -> 0 1 1 2")
    print("Explanation: Adds last two numbers to generate next.")

def find_max_min():
    print("Program: Find Max and Min")
    print("""
def find_max_min(lst):
    return max(lst), min(lst)""")
    print("Test Case 1: [1,5,3,8,2] -> (8, 1)")
    print("Test Case 2: [10, 20, 0] -> (20, 0)")
    print("Explanation: Uses built-in max() and min().")

def count_vowels():
    print("Program: Count Vowels")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for c in s if c in vowels)""")
    print("Test Case 1: 'apple' -> 2")
    print("Test Case 2: 'Hello World' -> 3")
    print("Explanation: Counts each vowel character in the string.")

def count_char_occurrence():
    print("Program: Count Character Occurrence")
    print("""
def count_char(s, ch):
    return s.count(ch)""")
    print("Test Case 1: ('banana', 'a') -> 3")
    print("Test Case 2: ('apple', 'p') -> 2")
    print("Explanation: Uses count() method to count character.")

def swap_variables():
    print("Program: Swap Two Variables")
    print("""
def swap(a, b):
    return b, a""")
    print("Test Case 1: swap(2, 3) -> (3, 2)")
    print("Test Case 2: swap(10, -1) -> (-1, 10)")
    print("Explanation: Uses tuple unpacking to swap values.")

def remove_duplicates():
    print("Program: Remove Duplicates from List")
    print("""
def remove_duplicates(lst):
    return list(set(lst))""")
    print("Test Case 1: [1,2,2,3] -> [1,2,3]")
    print("Test Case 2: [4,4,4,5,6] -> [4,5,6]")
    print("Explanation: Converts list to set to remove duplicates.")

def sum_of_list():
    print("Program: Sum of Elements in List")
    print("""
def sum_list(lst):
    return sum(lst)""")
    print("Test Case 1: [1,2,3] -> 6")
    print("Test Case 2: [10,-5,5] -> 10")
    print("Explanation: Uses built-in sum() to add list elements.")

def frequency_characters():
    print("Program: Frequency of Characters")
    print("""
    def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq""")
    print("Test Case 1: 'apple' -> {'a':1,'p':2,'l':1,'e':1}")
    print("Test Case 2: 'book' -> {'b':1,'o':2,'k':1}")
    print("Explanation: Uses dictionary to count each character.")

def sort_without_sort():
    print("Program: Sort List Without sort()")
    print("""
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst""")
    print("Test Case 1: [3,1,2] -> [1,2,3]")
    print("Test Case 2: [5,4,3] -> [3,4,5]")
    print("Explanation: Implements bubble sort to sort manually.")

def second_largest():
    print("Program: Second Largest Number")
    print("""
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
""")
    print("Test Case 1: [10,5,8,12,3] -> 10")
    print("Test Case 2: [4,1,7,3] -> 4")
    print("Explanation: Tracks first and second highest values.")

def is_prime():
    print("Program: Check Prime Number")
    print("""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
""")
    print("Test Case 1: 7 -> True")
    print("Test Case 2: 9 -> False")
    print("Explanation: Checks divisibility from 2 to sqrt(n).")