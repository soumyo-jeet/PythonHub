import pandas

with open("nato_phonetic_alphabet.csv") as np:
    df = pandas.read_csv(np)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
word_dict = {row.letter : row.code for (index , row) in df.iterrows()}

print(word_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Your Name: ").upper()

try:
    nato = [word_dict[letter] for letter in name]
    print(nato)
except KeyError:
    print("Invalid Typing")

