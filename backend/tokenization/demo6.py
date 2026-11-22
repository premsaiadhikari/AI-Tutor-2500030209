# word level Tokenization
text =input("Enter your sentence: ") or "Hello, how are you doing today?"
print("Original Text: ", text)
tokens = text.split()
print("Tokens: ", tokens)
print("Length of tokens:",len(tokens))
