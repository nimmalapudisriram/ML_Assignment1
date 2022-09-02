"""How many unique words have been used in the sentence? Use the split methods and set
to get the unique words """

sentence = "I am a teacher and I love to inspire and teach people"
txt = sentence.split(" ")  # splitting the sentence into words based on space using split() function
unique_words = set(txt)  # converting list into set using set() method

print("\nNo of unique words in the sentence: ",
      len(unique_words))  # set does not contain duplicate values so No. of unique words is equal to length of set
print("\nSet with unique words: ", unique_words)  # printing unique words set
