# Nova AI Generated Code
# Idea: Utility fonksiyonu seti
# Generated: 2025-06-18T19:59:58.981008

Aşağıdaki kod, utility fonksiyonu seti olarak adlandırılır ve çeşitli yardımcı işlevleri içerir.

```Python
class UtilityFunctions:
    def __init__(self):
        pass

    # String manipülasyon fonksiyonu
    def string_manipulation(self, string):
        return string.upper()

    # List slicing fonksiyonu
    def list_slicing(self, list, start, end):
        return list[start:end]

    # Dictionary manipulation fonksiyonu
    def dictionary_manipulation(self, dictionary, key):
        if key in dictionary:
            return dictionary[key]
        else:
            return "Key not found"

    # List sorting fonksiyonu
    def list_sorting(self, list):
        return sorted(list)

    # Tuple manipulation fonksiyonu
    def tuple_manipulation(self, tuple):
        return tuple[1:]

    # Set manipulation fonksiyonu
    def set_manipulation(self, set):
        return set.union({1, 2, 3})

    # Math operation fonksiyonu
    def math_operation(self, num1, num2, operation):
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 != 0:
                return num1 / num2