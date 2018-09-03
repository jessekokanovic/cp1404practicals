word_occurrences = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_occurrences[word] = word_occurrences.get(word, 0) + 1

words = sorted(word_occurrences.keys())
longest_word = max(len(word) for word in words)
for word in words:
    print("{:{x}} : {}".format(word, word_occurrences[word], x=longest_word))
