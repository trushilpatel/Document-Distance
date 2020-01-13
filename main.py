import utility
import os

print("Document Distance")
print("-" * 20)

file_directory = input("Enter the file directory : ")
files = list()

# getting list of files
for i in os.listdir(file_directory):
    files.append(os.path.join(file_directory, i))

totalFiles = len(files)

word_tockenized_file = list()

# word tokenizing
for file in files:
    word_tockenized_file.append(utility.transformData(file))

unique_words = set()
file_wise_words_stemming = list()

for f in word_tockenized_file:
    file_wise_words_stemming.append(utility.stemming(f))

for i in range(len(file_wise_words_stemming)):
    # sorting file wise unique words
    file_wise_words_stemming[i].sort()
    unique_words.update(file_wise_words_stemming[i])

# sorting the unique word list
unique_words = list(unique_words)
unique_words.sort()

total_unique_words = len(unique_words)
tf_idf_list = list()

for i in range(totalFiles):
    tf_idf_list.extend([[0] * total_unique_words].copy())

tf_idf_list = tf_idf_list.copy()
length_unique_words = len(unique_words)

for word in range(length_unique_words):
    for f in range(totalFiles):
        tf_idf_list[f][word] = file_wise_words_stemming[f].count(unique_words[word])

for i in tf_idf_list:
    print(i)

# Printing the similarity
print()
print("*" * 30)
print("Similarities of files : ")
print("*" * 30)

print("Cosine based implementation")
print("^" * 30)

for i in range(len(tf_idf_list)):
    print()
    print("File ", i + 1, " : ")
    print("-" * 20)

    for j in range(len(tf_idf_list)):
        if i != j:
            radian = utility.cosineDistance(tf_idf_list[i], tf_idf_list[j])
            print("Similarity with file ", j + 1, " : ", utility.radianToDegree(radian))

print()
print()
print("Euclidean based implementation")
print("^" * 30)

for i in range(len(tf_idf_list)):
    print()
    print("File ", i + 1, " : ")
    print("-" * 20)

    for j in range(len(tf_idf_list)):
        if i != j:
            print("Similarity with file ", j + 1, " : ", utility.euclideanDistance(tf_idf_list[i], tf_idf_list[j]))
