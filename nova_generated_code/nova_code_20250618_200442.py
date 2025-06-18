# Nova AI Generated Code
# Idea: Basit oyun mekaniği
# Generated: 2025-06-18T20:04:42.962875

Bu örnek, basit bir oyun mekaniği olan "Taş-Kağıt-Makas" oyununu simüle eden Python kodu olacaktır. Oyun, bir oyuncu tarafından seçilen Taş, Kağıt veya Makas sembolünü bilgisayar tarafından seçilen sembole karşı karşılaştırır. Oyuncunun seçimi bilgisayar tarafından seçilen sembolün üstün, eşit veya zayıf olur.

```python
import random

def oyun():
    choices = ["Taş", "Kağıt", "Makas"]
    computer = random.choice(choices)
    user = input("Taş, Kağıt veya Makas seçiniz: ").title()
    
    while user not in choices:
        user = input("Hatalı seçim. Taş, Kağıt veya Makas seçiniz: ").title()
    
    print(f"\nBilgisayar seçimi: {computer}")
    print(f"Oyuncu seçimi: {user}\n")

    if user == computer:
        print("Berabere!")
    elif (user == "Taş" and computer == "Makas") or (user == "Kağıt" and computer == "Taş") or (user == "Makas" and computer == "Kağıt"):
        print("Oyuncu kazandı!")
    else:
        print("Bilgisayar kazandı!")

if __name__ == "__main__":
    oyun()
```

Bu kod, oy