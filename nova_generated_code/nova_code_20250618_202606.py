# Nova AI Generated Code
# Idea: Veri analizi için yardımcı fonksiyon
# Generated: 2025-06-18T20:26:06.693390

Aşağıdaki kod, veri analizi için yardımcı bir fonksiyon oluşturur. Bu fonksiyon, verilen veri dizisinde istenen veri tipine göre veri analizi yapar.

```Python
import pandas as pd
import numpy as np

def veri_analizi(data, veri_tipi, istatistik):
    """
    Veri analizi için yardımcı fonksiyon.

    Args:
        data (list): Veri dizisi
        veri_tipi (str): Veri tipi (numeric, string, datetime)
        istatistik (str): İstediğimiz istatistik (mean, median, mode)

    Returns:
        result (float or str): İstediğimiz istatistik
    """
    # Veri dizisini pandas dataframeına çevir
    df = pd.DataFrame(data, columns=['veri'])

    # Veri tipine göre veri analizi yap
    if veri_tipi == 'numeric':
        if istatistik == 'mean':
            result = np.mean(df['veri'])
        elif istatistik == 'median':
            result = np.median(df['veri'])
        elif istatistik == 'mode':
            result = df['veri'].mode().values[0]
        else:
            raise ValueError("Geçersiz istatistik tipi")
    elif veri_tipi == 'string':
        if istatistik == 'mode':
            result = df['veri'].mode().values[