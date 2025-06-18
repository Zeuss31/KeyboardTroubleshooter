# Nova AI Generated Code
# Idea: Basit oyun mekaniği
# Generated: 2025-06-18T20:21:29.597347

Bir basit oyun mekaniği yazmak için, bir "Taş-Kağıt-Makas" oyununu yazalım. Oyun, kullanıcıdan bir seçim almaya çalışır ve bir rastgele seçim yapmaktadır. Kullanıcı, "Taş", "Kağıt" veya "Makas" seçebilir. Oyun, bu seçimlere göre sonuçlandırır.

Aşağıdaki kod, bu oyunu oluşturur:

```python
import random

def oyun():
    choices = ["Taş", "Kağıt", "Makas"]
    computer = random.choice(choices)

    user = input("Taş, Kağıt veya Makas seçin: ").title()

    while user not in choices:
        user = input("Hatalı seçim! Taş, Kağıt veya Makas seçin: ").title()

    print(f"\nBilgisayarın seçimi: {computer}")
    print(f"\nKullanıcın seçimi: {user}\n")

    if user == computer:
        print("Berabere!")
    elif (user == "Taş" and computer == "Makas") or (user == "Kağıt" and computer == "Taş") or (user == "Makas" and computer == "Kağıt"):
        print("Kullanıcı kazandı!")
    else:
        print("Bilgisayar kazandı!")

if __name__ ==