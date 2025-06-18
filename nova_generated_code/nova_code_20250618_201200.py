# Nova AI Generated Code
# Idea: Utility fonksiyonu seti
# Generated: 2025-06-18T20:12:00.622234

Bir utility fonksiyonu seti, Türkçe'de "yardımcı fonksiyonlar" olarak da bilinir. Bu fonksiyonlar, programlama dilinde sıkça kullanılan, tekrar tekrar yazılması gereken kod parçaslarını içerir. Aşağıdaki kod, bir utility fonksiyonu setini oluşturur:

```python
# Utility Fonksiyonu Seti

# 1. Fonksiyon: Tekrarlı karakter sayım
def karakter_sayim(text):
    karakter_count = {}
    for karakter in text:
        if karakter in karakter_count:
            karakter_count[karakter] += 1
        else:
            karakter_count[karakter] = 1
    return karakter_count

# 2. Fonksiyon: İki liste birleştirme
def liste_birlestirme(liste1, liste2):
    return liste1 + liste2

# 3. Fonksiyon: Listeyi tersine çevirme
def liste_tersine_cevir(liste):
    return liste[::-1]

# 4. Fonksiyon: İki liste kesişimi
def liste_kesisimi(liste1, liste2):
    return list(set(liste1) & set(liste2))

# 5. Fonksiyon: Liste içindeki en büyük sayıyı bulma
def liste_boyut_bul(liste):
    return max(liste)

# 6. Fonksiyon: Listeye rastgele bir eleman