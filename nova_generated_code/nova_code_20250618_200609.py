# Nova AI Generated Code
# Idea: Metin işleme aracı
# Generated: 2025-06-18T20:06:09.725243

Here is a Python code for a "Text Processing Tool" that performs the following operations:

1. Calculates the frequency of each word in the input text.
2. Removes punctuation marks from the text.
3. Converts the text to lowercase.
4. Removes stop words (common words like "the", "and", etc. that do not carry much meaning).

Here is the code:
```python
import re
from collections import Counter
import string

class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.stop_words = set(["the", "and", "a", "an", "in", "on", "at", "by", "with", "from", "to", "of", "for", "it", "is", "are", "am", "be", "been", "being"])

    def process_text(self):
        # Remove punctuation marks
        text_no_punct = re.sub('['+string.punctuation+']', '', self.text)

        # Convert to lowercase
        text_lower = text_no_punct.lower()

        # Remove stop words
        words = text_lower.split()
        words = [word for word in words if word not in self.stop_words]

        # Calculate word frequencies
        freq = Counter(words)

        return freq

# Test the code
text = "This is a sample text. It is a test text. The frequency of each word will be calculated."