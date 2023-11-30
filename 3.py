user_input = input("pynative: ")
even_index_chars = ""
for index, char in enumerate(user_input):
    if index % 2 == 0:
        even_index_chars += char
print("Characters at even index positions:", even_index_chars)
    