#Task 1 Lutfil
sentences = input("Please enter any sentences: ")

words = sentences.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_common_word = max(word_count, key=word_count.get)
max_count = word_count[most_common_word]

print(f"The most common word is: {most_common_word}")
print(f"Total words: {max_count}")



