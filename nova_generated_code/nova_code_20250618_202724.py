# Nova AI Generated Code
# Idea: Utility fonksiyonu seti
# Generated: 2025-06-18T20:27:24.373567

Aşağıdaki kod, utility fonksiyonu seti için bir örnek sunar. Bu fonksiyonlar, çeşitli işlevleri yerine getirmeye yardımcı olur ve çeşitli alanlarda kullanıma açık olurlar.

```Python
# Utility function set in Python

# 1. Unique elements from a list
def unique_elements(lst):
    return set(lst)

# 2. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 3. Check if a list is empty
def is_empty(lst):
    return len(lst) == 0

# 4. Check if a number is even
def is_even(n):
    return n % 2 == 0

# 5. Check if a number is odd
def is_odd(n):
    return n % 2 != 0

# 6. Reverse a string
def reverse_string(s):
    return s[::-1]

# 7. Find the maximum value in a list
def max_value(lst):
    return max(lst)

# 8. Find the minimum value in a list
def min_value(lst):
    return min(lst)

# 9. Find the sum of elements in a list
def sum_elements(lst):
    return sum(lst)

# 10. Check if a string contains a certain word
def contains_word(s, word):
    return word in s

# Example usage:
print(unique_elements([1, 2, 2,