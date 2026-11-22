word=input("Enter a word:") or "python"

print("Word:",word)
print("length of the word:",len(word))

Characters=list(word)

print("Characters in the given Word:",Characters)

pairs=list(zip(Characters,Characters[1:]))

print("Adjacent pairs:",pairs)
