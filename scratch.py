word_1 = "abc"
word_2 = "def"
word_1_split = list(word_1)
word_2_split = list(word_2)
combined = []
for x,y in zip(word_1_split, word_2_split):
    combined.append(x)
    combined.append(y)
# print(word_1_split)

# join the combined list into a string
combined_string 