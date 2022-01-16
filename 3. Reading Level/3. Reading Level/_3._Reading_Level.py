import math

Word = input("Enter the word: ").upper()
Words = Word.split(' ')

wordCount= len(Words)      
ChCount = 0
for i in range(0,len(Word)):
    if "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(Word[i]) >= 0:
        ChCount += 1

Avg = ChCount/ wordCount

print(Avg)



