word = input("Ingresa una palabra: ")
word_1 = list(word)

print("Es palindromo") if word == list(reversed(word_1)) else print("No es palindromo")

