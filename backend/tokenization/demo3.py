tokens=["java","python","html","Css"]
print("Tokens:",tokens)

print("Length of Tokens:",len(tokens))
print("First token:",tokens[0])
print("last token:",tokens[-1])
print("last token:",tokens[len(tokens)-1])

print("First two tokens:",tokens[0:2])
print("Tokens in reverse order:",tokens[::-1])
print("Last two tokens:",tokens[-2:])

for token in tokens:
    print(token,end=" ,")