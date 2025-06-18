# Nova AI Generated Code
# Idea: Metin işleme aracı
# Generated: 2025-06-18T20:16:49.536754

Aşağıdaki kod, metin işleme aracı için bir Python koduudur. Bu kod, kullanıcıdan alınan metni okur, paragraflarını ayırtır, kelimelerini sayar ve kelimenin uzunluğunu gösterir.

```python
# Metin işleme aracı

def metin_isleme():
    # Kullanıcıdan metin alma
    metin = input("Lütfen bir metin giriniz: ")

    # Paragrafları ayırtma
    paragraflar = metin.split("\n\n")

    # Paragrafları sayma
    paragraf_sayisi = len(paragraflar)
    print(f"Metin {paragraf_sayisi} paragraflıdır.")

    # Kelimeleri sayma
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    print(f"Metin {kelime_sayisi} kelime içerir.")

    # Kelimenin uzunluğunu gösterme
    for i, kelime in enumerate(kelimeler):
        kelime_uzunlugu = len(kelime)
        print(f"{i+1}. kelime: {kelime}, uzunluğu: {kelime_uzunlugu}")

metin_isleme()
```

Bu kod, kullanıcıdan alınan metni okur ve ardından onu paragraflarına ayırtır.