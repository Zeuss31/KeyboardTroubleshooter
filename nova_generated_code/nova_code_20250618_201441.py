# Nova AI Generated Code
# Idea: Basit oyun mekaniği
# Generated: 2025-06-18T20:14:41.674241

Basit oyun mekaniği yazmaya çalışalım. Bu/example, bir oyuncunun bir karakteri kontrol ederek, bir mayın tarlası oyununda mayınların patlamasını engellemek için çalışır.

**Oyun Mekaniği:**
Oyun, 5x5 boyutunda bir mayın tarlasıdır. Oyuncunun kontrol ettiği karakter, bir mayın tarlasına girmeye çalışır. Eğer karakter mayına dokunursa, oyun biter. Aksi takdirde, karakter mayının yakınına gider ve oyun devam eder.

**Python Kodu:**
```python
import random

# Oyun boyutu
BOYUT = 5

# Mayın boyutu
MAYIN_BOYUTU = 2

# Oyun alanını oluşturduk
mayin_tarlası = [[0 for _ in range(BOYUT)] for _ in range(BOYUT)]

# Mayınlar oluşturduk
for i in range(BOYUT):
    for j in range(BOYUT):
        if random.randint(0, 1):
            mayin_tarlası[i][j] = 1

# Oyuncunun kontrol ettiği karakter
karakter_x = 0
karakter_y = 0

# Oyuna başlayalım
while True:
    # Oyuncunun girdiği koordinatları alalım
    x = int(input("X ko