from itertools import count

alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
        num_vowles = 0
        for v in vowel:
            num_vowles = num_vowles + line.count(v)
        letter = alphabet[num_vowles]
        message += letter
    print(message)
