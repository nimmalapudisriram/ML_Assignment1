"""How many unique words have been used in the sentence? Use the split methods and set
to get the unique words """

sentence = "I am a teacher and I love to inspire and teach people"
txt = sentence.split(" ")
unique_words = set(txt)
print("\nNo of unique words in the sentence: ", len(unique_words))
print("\nSet with unique words: ", unique_words)