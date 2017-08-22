import math
import random
import os
import glob

#Markov Chain Essay Writer

path = "C:\\Users\\Baxter\\Documents\\GitHub\\markovEssayWriter\\text_examples\\*.txt"
files = glob.glob(path)
documents = []
for name in files:
    with open(name, "r") as f:
        documents.append(f.read())

output_array = []
next_word = []
output_text = ""

def random_array_item(arr):
    return arr[random.randint(0, len(arr) - 1)]

for i in range(len(documents)):
    documents[i] = documents[i].split()

output_array.append(random_array_item(documents)[0])

while True:
    for i in documents:
        for j in range(len(i)):
            if(i[j] == output_array[len(output_array)-1]):
                try:
                    next_word.append(i[j + 1])
                except:
                    next_word.append("")
    word_choice = random_array_item(next_word)
    output_array.append(word_choice)
    next_word = []
    if(word_choice == ""):
        break

for i in range(len(output_array)):
    if(i == len(output_array) - 1):
        output_text = output_text + output_array[i]
    else:
        output_text = output_text + output_array[i] + " "

print(output_text)
