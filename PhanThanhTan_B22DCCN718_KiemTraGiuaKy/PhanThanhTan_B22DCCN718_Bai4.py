import matplotlib.pyplot as plt
from collections import Counter

text = input()
words = text.split()
word_freq = Counter(words)

sorted_word_freq = dict(
    sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
top10_word_freq = dict(list(sorted_word_freq.items())[:10])

max_freq = max(top10_word_freq.values())
plt.figure(figsize=(10, 6))
plt.bar(top10_word_freq.keys(), top10_word_freq.values())
plt.xticks(rotation=90)
plt.yticks(range(0, max_freq + 1, 1))

plt.title("Biểu đồ tần suất xuất hiện của từ")
plt.xlabel("Từ")
plt.ylabel("Số lần xuất hiện")
plt.show()
