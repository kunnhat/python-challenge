import os

filepath = os.path.join("PythonText2.txt")

with open(filepath) as text:
    a = text.read()
words = len([word for word in a.split(sep=" ")])
sentences = len([word for word in a if word == "."]) + len([word for word in a if word == "?"]) +  len([word for word in a if word == "!"])
average_sentence_length = words / sentences
average_letter = len([letter for letter in a if letter.isalpha()])/words

print(f'Paragraph Analytics')
print(f'-----------------------')
print(f'Approximate word count: {words}')
print(f'Approximate sentence count: {sentences}')
print(f'Average letter count: {format(average_letter, ".2f")}')
print(f'Average sentence length {format(average_sentence_length, ".2f")}')

output = os.path.join("Text 2 Analytics.txt")
with open(output, 'w') as text:
    text.write(f"Paragraph Analysis")
    text.write("\n")
    text.write(f"-----------------")
    text.write("\n")
    text.write(f"Approximate word count: {words}")
    text.write("\n")
    text.write(f"Approximate sentence count: {sentences}")
    text.write("\n")
    text.write(f"Average letter count: {format(average_letter, '.2f')}")
    text.write("\n")
    text.write(f"Average sentence length: {format(average_sentence_length, '.2f')}")