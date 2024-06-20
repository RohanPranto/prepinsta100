#print the words that has more character than Z in a sentence

sentence = input("Enter sentence : ")
words = sentence.split()
threshold = int(input("Enter threshold: "))
for i in words:
    if len(i) > threshold:
        print(i)
