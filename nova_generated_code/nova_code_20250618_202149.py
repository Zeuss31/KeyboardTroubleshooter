# Nova AI Generated Code
# Idea: Utility fonksiyonu seti
# Generated: 2025-06-18T20:21:49.788902

Aşağıdaki Python kodunuz, utility fonksiyonu seti olarak adlandırılan bir koleksiyondur. Bu koleksiyon, farklı amaçlar için kullanılan çeşitli utility fonksiyonlarını içerir.

```python
# Utility Fonksiyonu Seti

# 1. Fonksiyon: Sayının tek mi çift mi kontrolu
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 2. Fonksiyon: İki sayıyı karşılaştırma
def compare_numbers(a, b):
    if a > b:
        return f"{a} greater than {b}"
    elif a < b:
        return f"{a} smaller than {b}"
    else:
        return f"{a} equal to {b}"

# 3. Fonksiyon: Liste içerisindeki en büyük sayı bulma
def find_max(lst):
    return max(lst)

# 4. Fonksiyon: Liste içerisindeki en küçük sayı bulma
def find_min(lst):
    return min(lst)

# 5. Fonksiyon: Liste içerisindeki ortalama hesaplama
def find_average(lst):
    return sum(lst) / len(lst)

# 6. Fonksiyon: İki liste birleştirme
def merge_lists(lst1, lst2):
    return lst1 + lst2

# 7. Fonksiyon: Liste içerisindeki tekrar eden sayı bulma
def find_duplicates(lst):
    return