# Nova AI Generated Code
# Idea: Basit bir algoritma optimizasyonu
# Generated: 2025-06-18T20:08:07.473837

Algoritma optimizasyonunu göstermek için, bir örnek verelim. Bu örnek, bir listeyi sıralama algoritmasını optimize edecektir.

**Örnek Kod:**
```python
import time

# Liste oluşturma
liste = [64, 34, 25, 12, 22, 11, 90]

# Basit algoritma ( Bubble Sort )
def bubble_sort(liste):
    n = len(liste)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Optimized algoritma ( Timsort )
import heapq
def timsort(liste):
    return sorted(liste)

# Basit algoritma ile liste sıralama
start_time = time.time()
liste = bubble_sort(liste)
print("Basit algoritma ile sıralama:", liste)
end_time = time.time()
print("Basit algoritma süresi:", end_time - start_time, "saniye")

# Optimized algoritma ile liste sıralama
start_time = time.time()
liste = timsort(liste)
print("Optimized algoritma ile sıralama:", liste)
end_time = time.time()
print("Optimized algoritma süresi