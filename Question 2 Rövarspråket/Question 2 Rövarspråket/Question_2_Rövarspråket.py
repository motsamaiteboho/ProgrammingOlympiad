
Phrase = input("Phrase: ").lower();

NewPhrase = "";
for i in range(0, len(Phrase)):
      if ("aeiou".find(Phrase[i]) >=0) or Phrase[i] == ' ' :
          NewPhrase += Phrase[i]
      else:
          NewPhrase += Phrase[i] + 'o' + Phrase[i]

print(NewPhrase)
